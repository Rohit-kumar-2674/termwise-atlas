# Configuration examples

Copy only the example for your chosen client, review it, and replace model placeholders with current supported IDs. Never overwrite a working configuration without a backup. These files contain no credentials and do not automatically configure your shell.

| Example | Intended consumer | Loading behavior |
| --- | --- | --- |
| `openrouter.env.example` | Aider / compatible provider clients | Client-specific `.env` support or process environment |
| `ollama.env.example` | Aider client; Ollama server setting | Set server variable on server, client URL on client |
| `gemini.env.example` | Gemini CLI API route | Follow current CLI authentication docs |
| `generic-openai-compatible.env.example` | Schematic compatible client | Names/protocol vary; not universal auto-configuration |
| `continue-*.yaml.example` | Continue config schema v1 | Explicit `cn --config PATH` or documented IDE config |
| `opencode-ollama.json.example` | OpenCode local provider | Merge into documented `opencode.json`; model needs RAM |
| `codex-openrouter.toml.example` | Codex custom provider | Merge into your config; metadata caveat documented |

[Key handling](../docs/security/api-keys.md) · [Routing and limitations](../docs/providers/routing.md)
