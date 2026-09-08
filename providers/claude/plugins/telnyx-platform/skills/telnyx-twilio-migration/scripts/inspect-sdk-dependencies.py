#!/usr/bin/env python3
"""Read local dependency declarations; never resolve packages over the network.

Exit zero only for positive evidence. Unresolved external Maven parents,
properties, and unsupported Gradle expressions deliberately remain warnings.
Gradle version catalogs use stdlib tomllib on Python 3.11+; older Python still
supports Maven, Composer and literal Gradle coordinates without extra packages.
"""
from __future__ import annotations

import json
import importlib.util
import os
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

try:
    import tomllib
except ImportError:
    tomllib = None

JVM_ARTIFACTS = {"telnyx", "telnyx-core", "telnyx-client-okhttp"}


def version_is_constrained(value: object) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(
        r"\d+\.\d+(?:[.][0-9]+)*(?:-[A-Za-z0-9][A-Za-z0-9.-]*)?", value.strip()
    ))


def composer_declared(root: Path, package: str = "telnyx/telnyx-php") -> bool:
    try:
        data = json.loads((root / "composer.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return isinstance(data, dict) and any(
        isinstance(data.get(section), dict)
        and isinstance(data[section].get(package), str)
        and bool(data[section][package].strip())
        for section in ("require", "require-dev")
    )


def maven_dependencies(path: Path) -> list[tuple[str, str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
        # Manifests need no entities. Avoid entity expansion on untrusted input.
        if "<!DOCTYPE" in text or "<!ENTITY" in text:
            return []
        project = ET.fromstring(text)
    except (OSError, ValueError, ET.ParseError):
        return []
    for node in project.iter():
        node.tag = node.tag.rsplit("}", 1)[-1]
    if project.tag != "project":
        return []
    properties = {node.tag: (node.text or "").strip()
                  for node in project.findall("./properties/*")}

    def resolve(value: str) -> str:
        seen = set()
        while re.fullmatch(r"\$\{[^}]+\}", value) and value not in seen:
            seen.add(value)
            value = properties.get(value[2:-1], "")
        return value

    def field(node: ET.Element, name: str) -> str:
        return resolve((node.findtext(name) or "").strip())

    managed = {
        (field(dep, "groupId"), field(dep, "artifactId")): field(dep, "version")
        for dep in project.findall("./dependencyManagement/dependencies/dependency")
    }
    dependencies = []
    for dep in project.findall("./dependencies/dependency"):
        group, artifact = field(dep, "groupId"), field(dep, "artifactId")
        # An explicit unresolved version must not fall back to management.
        version = (field(dep, "version") if dep.find("version") is not None
                   else managed.get((group, artifact), ""))
        dependencies.append((group, artifact, version))
    return dependencies


def maven_pinned(path: Path) -> bool:
    return any(group == "com.telnyx.sdk" and artifact in JVM_ARTIFACTS
               and version_is_constrained(version)
               for group, artifact, version in maven_dependencies(path))


def groovy_slashy_ranges(source: str, code: str) -> list[tuple[int, int]]:
    """Exclude Groovy's additional string delimiters from declaration evidence.

    Ordinary quotes/comments are already masked by the shared lexer. Slashy
    strings are expressions, so a division operator after an operand isn't an
    opener. This does not evaluate interpolation or arbitrary build programs.
    """
    ranges = []
    end = 0
    for match in re.finditer(r"\$/|/(?![/*])", code):
        start = match.start()
        if start < end:
            continue
        dollar = match[0] == "$/"
        prefix = code[:start].rstrip()
        if not dollar and prefix and prefix[-1] not in "=(:,[!?{" and not re.search(r"\breturn$", prefix):
            continue
        cursor = match.end()
        while cursor < len(source):
            if dollar and source.startswith("/$", cursor):
                cursor += 2
                break
            if not dollar and source[cursor] == "/":
                cursor += 1
                break
            if (dollar and source[cursor] == "$" and cursor + 1 < len(source)
                    and source[cursor + 1] in "$/") or (not dollar and source[cursor] == "\\"):
                cursor += 2
            else:
                cursor += 1
        end = cursor
        ranges.append((start, end))
    return ranges


def gradle_dependencies(root: Path, catalog_root: Path | None = None) -> list[tuple[str, str, object]]:
    spec = importlib.util.spec_from_file_location(
        "sdk_source_ownership", Path(__file__).with_name("sdk-source-ownership.py"))
    ownership = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ownership)
    analyzer = ownership.load_script("lint-required-messaging-profile")
    dependencies = []
    accessors = set()
    for name in ("build.gradle", "build.gradle.kts"):
        try:
            source = (root / name).read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        # Reuse source masking: inline comments and help strings aren't code.
        lexed = ownership.lexed_source(source, ".kt" if name.endswith(".kts") else ".java")
        strings = {token.start: token for token in lexed.strings}
        inert_ranges = groovy_slashy_ranges(source, lexed.code) if name == "build.gradle" else []
        declaration = r"\b(?:implementation|api|compileOnly|runtimeOnly|testImplementation)\b"
        for match in re.finditer(declaration, lexed.code):
            if any(start <= match.start() < end for start, end in inert_ranges):
                continue
            prefix = re.match(r"\s*\(?\s*", lexed.without_comments[match.end():])
            start = match.end() + prefix.end()
            token = strings.get(start)
            if token:
                parts = token.contents.split(":")
                if len(parts) in {2, 3}:
                    dependencies.append((parts[0], parts[1], parts[2] if len(parts) == 3 else ""))
            else:
                accessor = re.match(r"libs\.([\w.]+)", lexed.code[start:])
                if accessor:
                    accessors.add(accessor[1])
                    continue
                # Groovy also accepts named-map dependency notation:
                # implementation group: 'g', name: 'a', version: '1.2.3'
                # and the equivalent parenthesized call. Read only string
                # tokens belonging to this declaration, so comments and prose
                # cannot contribute coordinates.
                cursor = match.end()
                while (cursor < len(lexed.code)
                       and lexed.code[cursor] in " \t\r"):
                    cursor += 1
                parenthesized = (cursor < len(lexed.code)
                                 and lexed.code[cursor] == "(")
                if parenthesized:
                    closing = analyzer.matching_delimiter(
                        lexed.code, cursor, "(", ")")
                    if closing is None:
                        continue
                    argument_start, argument_end = cursor + 1, closing
                else:
                    argument_start, argument_end = cursor, len(lexed.code)
                fields = {}
                cursor = argument_start
                continued = parenthesized
                while cursor < argument_end:
                    while (cursor < argument_end
                           and lexed.code[cursor].isspace()
                           and (continued or lexed.code[cursor] != "\n")):
                        cursor += 1
                    field = re.match(r"(group|name|version)\s*:",
                                     lexed.code[cursor:argument_end])
                    if field is None:
                        break
                    value_start = cursor + field.end()
                    while (value_start < argument_end
                           and lexed.without_comments[value_start].isspace()):
                        value_start += 1
                    token = strings.get(value_start)
                    if token and token.end <= argument_end:
                        fields[field[1]] = token.contents
                        cursor = token.end
                    else:
                        # Dynamic/unsupported values invalidate an earlier
                        # duplicate literal instead of leaving stale evidence.
                        fields[field[1]] = None
                        boundary = re.search(r"[,;\n})]",
                                             lexed.code[value_start:argument_end])
                        cursor = (argument_end if boundary is None else
                                  value_start + boundary.start())
                    while (cursor < argument_end
                           and lexed.code[cursor] in " \t\r"):
                        cursor += 1
                    if cursor >= argument_end or lexed.code[cursor] != ",":
                        break
                    cursor += 1
                    continued = True
                if "group" in fields and "name" in fields:
                    dependencies.append((fields["group"], fields["name"],
                                         fields.get("version", "")))
    if tomllib is None:
        return dependencies
    try:
        catalog = tomllib.loads(((catalog_root or root) / "gradle/libs.versions.toml").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return dependencies
    libraries, versions = catalog.get("libraries", {}), catalog.get("versions", {})
    if not isinstance(libraries, dict) or not isinstance(versions, dict):
        return dependencies
    for alias, entry in libraries.items():
        accessor = re.sub(r"[-_]", ".", alias)
        if accessor not in accessors:
            continue
        if isinstance(entry, str):
            parts = entry.split(":")
            if len(parts) != 3:
                continue
            group, artifact, version = parts
        elif isinstance(entry, dict):
            module = entry.get("module")
            if isinstance(module, str) and module.count(":") == 1:
                group, artifact = module.split(":")
            else:
                group, artifact = entry.get("group"), entry.get("name")
            version = entry.get("version")
            if isinstance(version, dict):
                reference = version.get("ref")
                version = versions.get(reference) if isinstance(reference, str) else None
        else:
            continue
        dependencies.append((group, artifact, version))
    return dependencies


def gradle_pinned(root: Path) -> bool:
    return any(group == "com.telnyx.sdk" and artifact in JVM_ARTIFACTS
               and version_is_constrained(version)
               for group, artifact, version in gradle_dependencies(root))


def jvm_declared(root: Path, vendor: str) -> bool:
    for directory, dirs, names in os.walk(root):
        relative = Path(directory).relative_to(root)
        dirs[:] = [name for name in dirs if name not in {
            ".git", "node_modules", "build", "vendor", ".gradle", ".venv"}
            and len(relative.parts) < 3]
        path = Path(directory)
        dependencies = maven_dependencies(path / "pom.xml") if "pom.xml" in names else []
        if "build.gradle" in names or "build.gradle.kts" in names:
            dependencies.extend(gradle_dependencies(path, root))
        if any((group == "com.telnyx.sdk" and artifact in JVM_ARTIFACTS)
               if vendor == "telnyx" else (group == "com.twilio.sdk" and artifact == "twilio")
               for group, artifact, _ in dependencies):
            return True
    return False


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in {"composer", "jvm-pinned", "jvm-declared", "twilio-jvm-declared"}:
        return 2
    root = Path(sys.argv[2])
    mode = sys.argv[1]
    if mode == "composer":
        found = composer_declared(root)
    elif mode.endswith("declared"):
        found = jvm_declared(root, "twilio" if mode.startswith("twilio") else "telnyx")
    else:
        found = maven_pinned(root / "pom.xml") or gradle_pinned(root)
    return 0 if found else 1


if __name__ == "__main__":
    sys.exit(main())
