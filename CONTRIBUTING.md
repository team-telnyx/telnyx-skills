# Contributing

Contributions of any kind are welcome! If you've found a bug or have a feature request, please feel free to [open an issue](/issues).

To make changes yourself, follow these steps:

1. [Fork](https://help.github.com/articles/fork-a-repo/) this repository and [clone](https://help.github.com/articles/cloning-a-repository/) it locally.
2. Make your changes
3. Test your changes (see below)
4. Submit a [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)

## What's in this repo

| Directory | What it contains | How to test |
|-----------|-----------------|-------------|
| `tools/python/` | Python agent toolkit (PyPI) | `cd tools/python && pip install -e ".[dev]" && pytest` |
| `tools/typescript/` | TypeScript agent toolkit (npm) | `cd tools/typescript && npm ci && npm test` |
| `tools/mcp/` | MCP proxy server (npm) | `cd tools/mcp && npm ci && npm run build` |
| `cli/` | Agent CLI | `cd cli && npm ci && npm test` |
| `skills/` | Agent skills (SKILL.md files) | See "Skills" below |
| `guides/` | Operational guides | `npm run test:guides` |

## Skills

Skills in `skills/` are the canonical source. They are synced to `providers/claude/plugin/skills/` and `providers/cursor/plugin/skills/` via `scripts/sync-skills.sh`. After modifying skills, run:

```bash
./scripts/sync-skills.sh
```

You can verify sync locally with `./scripts/check-skills-sync.sh`.

### Auto-generated skills

Most skills are automatically generated from Telnyx OpenAPI specifications. Do not modify code examples directly — they will be overwritten on the next generation. If you find an error in a code example, it needs to be fixed in the upstream OpenAPI spec.

### Hand-authored skills

Skills in `telnyx-twilio-migration/`, `telnyx-webrtc-client/`, and `telnyx-import-voice-ai/` are manually authored. PRs to improve these are welcome.

## Questions?

- For API questions, visit [support.telnyx.com](https://support.telnyx.com)
- For skill specification questions, see [agentskills.io](https://agentskills.io)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
