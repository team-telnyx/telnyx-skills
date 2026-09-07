/** Mock-binary coverage for the v0.30 telephony credential token action. */
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { chmodSync, existsSync, mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const cliRoot = join(__dirname, "..");
const cliBin = join(cliRoot, "bin", "telnyx-agent.ts");

function setupFakeTelnyx(version = "0.30.0", fail = false): { env: NodeJS.ProcessEnv; logPath: string } {
  const tempDir = mkdtempSync(join(tmpdir(), "telnyx-agent-credential-token-"));
  const binDir = join(tempDir, "bin");
  const logPath = join(tempDir, "args.jsonl");
  const fakeTelnyx = join(binDir, "telnyx");
  mkdirSync(binDir, { recursive: true });
  writeFileSync(fakeTelnyx, `#!/usr/bin/env node
const fs = require("node:fs");
const args = process.argv.slice(2);
if (args[0] === "--version") { console.log("telnyx version ${version}"); process.exit(0); }
fs.appendFileSync(process.env.TELNYX_FAKE_ARGS_LOG, JSON.stringify(args) + "\\n");
if (${JSON.stringify(fail)}) {
  process.stdout.write("eyJ.private.payload-must-not-leak");
  process.stderr.write("private-error-payload-must-not-leak");
  process.exit(9);
}
process.stdout.write("eyJhbGciOiJIUzI1NiJ9.payload.signature\\n");
`);
  chmodSync(fakeTelnyx, 0o755);
  return { env: { ...process.env, TELNYX_CLI_PATH: fakeTelnyx, TELNYX_FAKE_ARGS_LOG: logPath }, logPath };
}

function runAgent(args: string[], env: NodeJS.ProcessEnv): { status: number; stdout: string; stderr: string } {
  try {
    const stdout = execFileSync(process.execPath, ["--import", "tsx", cliBin, ...args], { cwd: cliRoot, encoding: "utf8", env, timeout: 30_000 });
    return { status: 0, stdout, stderr: "" };
  } catch (err: any) {
    return { status: err.status ?? 1, stdout: err.stdout?.toString() ?? "", stderr: err.stderr?.toString() ?? "" };
  }
}

function loggedArgs(logPath: string): string[][] {
  if (!existsSync(logPath)) return [];
  const content = readFileSync(logPath, "utf8");
  assert.ok(content.endsWith("\n"), "fake binary JSONL must use a real newline terminator");
  return content.trimEnd().split("\n").map((line) => JSON.parse(line) as string[]);
}

describe("create-telephony-credential-token", () => {
  it("routes the exact v0.30 generated action and preserves the raw JWT only in explicit JSON output", () => {
    const fake = setupFakeTelnyx();
    const result = runAgent(["create-telephony-credential-token", "--id", "cred_123", "--json"], fake.env);
    assert.equal(result.status, 0, result.stderr);
    assert.deepEqual(JSON.parse(result.stdout), {
      credential_id: "cred_123",
      jwt: "eyJhbGciOiJIUzI1NiJ9.payload.signature\n",
    });
    assert.deepEqual(loggedArgs(fake.logPath), [
      ["telephony-credentials", "create-token", "--id", "cred_123", "--format", "raw"],
    ]);
  });

  it("does not print the JWT in human output", () => {
    const fake = setupFakeTelnyx();
    const result = runAgent(["create-telephony-credential-token", "--id", "cred_123"], fake.env);
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /received but hidden/);
    assert.doesNotMatch(result.stdout, /eyJhbGciOiJIUzI1NiJ9\.payload\.signature/);
  });

  it("requires a v0.30 Go CLI with an actionable upgrade message before dispatch", () => {
    const fake = setupFakeTelnyx("0.27.0");
    const result = runAgent(["create-telephony-credential-token", "--id", "cred_123", "--json"], fake.env);
    assert.equal(result.status, 1);
    assert.match(result.stdout, /requires >= 0\.30\.0/);
    assert.match(result.stdout, /npm install|go install|TELNYX_CLI_PATH/);
    assert.deepEqual(loggedArgs(fake.logPath), []);
  });

  it("does not leak a partial JWT when the generated action fails", () => {
    for (const outputFlag of [[], ["--json"]]) {
      const fake = setupFakeTelnyx("0.30.0", true);
      const result = runAgent(["create-telephony-credential-token", "--id", "cred_123", ...outputFlag], fake.env);
      assert.equal(result.status, 1);
      assert.doesNotMatch(`${result.stdout}${result.stderr}`, /payload-must-not-leak/);
      assert.match(`${result.stdout}${result.stderr}`, /sensitive response output was suppressed/);
    }
  });

  it("rejects missing or valueless --id before dispatch", () => {
    for (const args of [
      ["create-telephony-credential-token", "--json"],
      ["create-telephony-credential-token", "--id", "--json"],
    ]) {
      const fake = setupFakeTelnyx();
      const result = runAgent(args, fake.env);
      assert.equal(result.status, 1);
      assert.match(result.stdout, /--id is required/);
      assert.deepEqual(loggedArgs(fake.logPath), []);
    }
  });

  it("renders help without dispatching the generated action", () => {
    const fake = setupFakeTelnyx();
    const result = runAgent(["create-telephony-credential-token", "--help"], fake.env);
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /create-telephony-credential-token/);
    assert.deepEqual(loggedArgs(fake.logPath), []);
  });

  it("advertises the capability as a v0.30 sensitive-output command", () => {
    const fake = setupFakeTelnyx();
    const result = runAgent(["capabilities", "--json"], fake.env);
    assert.equal(result.status, 0, result.stderr);
    const capabilities = JSON.parse(result.stdout);
    const voice = capabilities.api_capabilities["📞 Voice"] as Array<{ actions: string[] }>;
    assert.ok(voice.some((capability) => capability.actions.includes("create_telephony_credential_token")));
  });
});
