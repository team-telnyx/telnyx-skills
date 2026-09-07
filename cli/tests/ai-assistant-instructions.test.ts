/**
 * Mock-binary coverage for assistant instruction enhancement.
 */
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { chmodSync, existsSync, mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const cliRoot = join(__dirname, "..");
const cliBin = join(cliRoot, "bin", "telnyx-agent.ts");
const RAW_ENHANCEMENT_BODY = "event: instruction.delta\ndata: {\"instructions\":\"Keep escalation context.\"}\n\n{\"finish_reason\":\"stop\"}\n";

function setupFakeTelnyx(
  version = "0.30.0",
  failEnhancement = false,
): { logPath: string; env: NodeJS.ProcessEnv } {
  const tempDir = mkdtempSync(join(tmpdir(), "telnyx-agent-ai-assistant-instructions-"));
  const binDir = join(tempDir, "bin");
  const logPath = join(tempDir, "args.jsonl");
  const fakeTelnyx = join(binDir, "telnyx");
  mkdirSync(binDir, { recursive: true });

  writeFileSync(
    fakeTelnyx,
    `#!/usr/bin/env node
const fs = require("node:fs");
const args = process.argv.slice(2);
if (args[0] === "--version") { console.log(${JSON.stringify(`telnyx version ${version}`)}); process.exit(0); }
fs.appendFileSync(process.env.TELNYX_FAKE_ARGS_LOG, JSON.stringify(args) + "\\n");
if (args[0] !== "ai:assistants:instructions" || args[1] !== "enhance") {
  console.error("unexpected fake telnyx invocation: " + args.join(" "));
  process.exit(2);
}
if (${failEnhancement ? "true" : "false"}) {
  console.log("do not expose current instructions");
  console.error("enhancement unavailable");
  process.exit(1);
}
process.stdout.write(Buffer.from(${JSON.stringify(RAW_ENHANCEMENT_BODY)}, "utf8"));
`,
  );
  chmodSync(fakeTelnyx, 0o755);

  return {
    logPath,
    env: {
      ...process.env,
      TELNYX_CLI_PATH: fakeTelnyx,
      TELNYX_FAKE_ARGS_LOG: logPath,
      TELNYX_API_KEY: "KEY_fake_test",
    },
  };
}

function runAgent(
  args: string[],
  env: NodeJS.ProcessEnv,
): { stdout: string; stderr: string; status: number } {
  try {
    const stdout = execFileSync(process.execPath, ["--import", "tsx", cliBin, ...args], {
      cwd: cliRoot,
      encoding: "utf8",
      env,
      timeout: 30_000,
    });
    return { stdout, stderr: "", status: 0 };
  } catch (err: any) {
    return {
      stdout: err.stdout?.toString() ?? "",
      stderr: err.stderr?.toString() ?? "",
      status: err.status ?? 1,
    };
  }
}

function loggedArgs(logPath: string): string[][] {
  if (!existsSync(logPath)) return [];
  const contents = readFileSync(logPath, "utf8");
  assert.ok(contents.endsWith("\n"), "fake binary should terminate each JSON record with one newline");
  assert.ok(!contents.endsWith("\n\n"), "fake binary should not write a blank JSONL record");
  return contents.trimEnd().split("\n").map((line) => JSON.parse(line) as string[]);
}

describe("AI assistant instruction enhancement", () => {
  it("forwards the exact upstream action and preserves JSON/SSE-looking response content in structured JSON", () => {
    const fake = setupFakeTelnyx();
    const result = runAgent([
      "enhance-ai-assistant-instructions",
      "--assistant-id", "assistant-1",
      "--enhancement-prompt", "Make escalation rules explicit",
      "--instructions", "Escalate urgent issues",
      "--json",
    ], fake.env);

    assert.equal(result.status, 0, result.stderr);
    assert.deepEqual(JSON.parse(result.stdout), {
      assistant_id: "assistant-1",
      response: RAW_ENHANCEMENT_BODY,
      applied: false,
    });
    assert.deepEqual(loggedArgs(fake.logPath), [[
      "ai:assistants:instructions",
      "enhance",
      "--assistant-id",
      "assistant-1",
      "--enhancement-prompt",
      "Make escalation rules explicit",
      "--instructions",
      "Escalate urgent issues",
      "--format",
      "raw",
    ]]);
  });

  it("uses the assistant's current instructions when optional enhancement inputs are omitted", () => {
    const fake = setupFakeTelnyx();
    const result = runAgent([
      "enhance-ai-assistant-instructions",
      "--assistant-id", "assistant-1",
    ], fake.env);

    assert.equal(result.status, 0, result.stderr);
    assert.equal(result.stdout, RAW_ENHANCEMENT_BODY);
    assert.deepEqual(loggedArgs(fake.logPath), [[
      "ai:assistants:instructions",
      "enhance",
      "--assistant-id",
      "assistant-1",
      "--format",
      "raw",
    ]]);
  });

  it("rejects missing or valueless inputs before requesting enhancement", () => {
    const invalidCases = [
      ["enhance-ai-assistant-instructions", "--json"],
      ["enhance-ai-assistant-instructions", "--assistant-id", "", "--json"],
      ["enhance-ai-assistant-instructions", "--assistant-id", "assistant-1", "--enhancement-prompt", "--json"],
      ["enhance-ai-assistant-instructions", "--assistant-id", "assistant-1", "--instructions", "--json"],
    ];

    for (const args of invalidCases) {
      const fake = setupFakeTelnyx();
      const result = runAgent(args, fake.env);
      assert.notEqual(result.status, 0, `expected ${args.join(" ")} to fail`);
      assert.ok(JSON.parse(result.stdout).error);
      assert.deepEqual(loggedArgs(fake.logPath), []);
    }
  });

  it("rejects a pre-v0.30 Go CLI before making the enhancement request", () => {
    const fake = setupFakeTelnyx("0.29.0");
    const result = runAgent([
      "enhance-ai-assistant-instructions",
      "--assistant-id", "assistant-1",
      "--json",
    ], fake.env);

    assert.notEqual(result.status, 0);
    assert.match(JSON.parse(result.stdout).error, /Telnyx Go CLI 0\.29\.0, but this command requires >= 0\.30\.0/);
    assert.deepEqual(loggedArgs(fake.logPath), []);
  });

  it("reports Go CLI errors without trying to parse an enhancement response", () => {
    const fake = setupFakeTelnyx("0.30.0", true);
    const result = runAgent([
      "enhance-ai-assistant-instructions",
      "--assistant-id", "assistant-1",
      "--json",
    ], fake.env);

    assert.notEqual(result.status, 0);
    const error = JSON.parse(result.stdout).error;
    assert.match(error, /telnyx CLI failed while producing a raw response/);
    assert.doesNotMatch(error, /do not expose current instructions|enhancement unavailable/);
    assert.deepEqual(loggedArgs(fake.logPath), [[
      "ai:assistants:instructions",
      "enhance",
      "--assistant-id",
      "assistant-1",
      "--format",
      "raw",
    ]]);
  });
});
