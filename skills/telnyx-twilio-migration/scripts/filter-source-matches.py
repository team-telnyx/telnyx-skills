#!/usr/bin/env python3
"""Filter ``grep -nH`` matches through the migration source lexer.

The shell validators use grep for breadth, but grep cannot distinguish live
syntax from comments or quoted prose.  This adapter keeps the shell tools on
the same lexical contract as the messaging-profile analyzer while preserving
the familiar ``path:line:text`` output used in reports.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path


MATCH_RE = re.compile(r"^(.*?):([0-9]+):(.*)$")


def load_analyzer(path: Path):
    spec = importlib.util.spec_from_file_location("telnyx_source_contract", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("comments", "code"), default="comments")
    parser.add_argument("--analyzer", type=Path, required=True)
    parser.add_argument("--pattern", required=True)
    parser.add_argument("--region", choices=("all", "backend"), default="all")
    args = parser.parse_args()

    analyzer = load_analyzer(args.analyzer)
    cache: dict[Path, object] = {}
    for raw in sys.stdin:
        raw = raw.rstrip("\n")
        match = MATCH_RE.match(raw)
        if not match:
            continue
        filename, line_number, original = match.groups()
        path = Path(filename)
        try:
            if path not in cache:
                source = path.read_text(encoding="utf-8", errors="replace")
                if args.region == "backend":
                    source = analyzer.backend_executable_source(path, source)
                else:
                    source = analyzer.executable_source(path, source)
                suffix = analyzer.canonical_suffix(path)
                if (
                    path.name == ".env"
                    or path.name.startswith(".env.")
                    or path.suffix.lower() in {
                        ".conf",
                        ".env",
                        ".ini",
                        ".properties",
                        ".toml",
                        ".yaml",
                        ".yml",
                    }
                ):
                    suffix = ".sh"
                cache[path] = analyzer.lex_source(source, suffix)
            lexed = cache[path]
            view = lexed.code if args.mode == "code" else lexed.without_comments
            lines = view.splitlines()
            index = int(line_number) - 1
            filtered = lines[index] if 0 <= index < len(lines) else ""
        except OSError:
            filtered = original
        live_match = subprocess.run(
            ["grep", "-E", "-q", args.pattern],
            input=filtered,
            text=True,
            check=False,
        ).returncode == 0
        if filtered.strip() and live_match:
            print(f"{filename}:{line_number}:{filtered}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
