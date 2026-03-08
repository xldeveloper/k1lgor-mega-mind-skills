# Installing Mega-Mind Skills

This guide covers how to install the Mega-Mind skill set into your project so it is available to your AI coding assistant (Antigravity, GitHub Copilot, etc.).

---

## Step 1 — Install the CLI tool

Choose the method that fits your workflow:

### pip (standard)

```bash
pip install mega-mind-orchestrator
```

### pipx (recommended — isolated install, globally available)

```bash
pipx install mega-mind-orchestrator
```

### uv

```bash
uvx --from mega-mind-orchestrator mega-mind
```

---

## Step 2 — Initialize skills in your project

Navigate to your project root and run:

```bash
mega-mind init
```

This copies the full `.agent/` directory — containing all 42 skills, workflows, and agent definitions — into your project.

### For GitHub Copilot (VS Code)

To also install in the format GitHub Copilot expects, add the `--copilot` flag:

```bash
mega-mind init --copilot
```

This installs **both**:

- `.agent/` — for Antigravity, Cursor, Claude Code, and other AI tools
- `.github/` — for GitHub Copilot in VS Code

### Target a specific directory

```bash
mega-mind init /path/to/your/project
mega-mind init /path/to/your/project --copilot
```

### Overwrite an existing installation

```bash
mega-mind init --force
mega-mind init --copilot --force
```

> ⚠️ `--force` overwrites the existing directories completely.

---

## What gets installed

### Standard install (`mega-mind init`)

```
your-project/
└── .agent/
    ├── AGENTS.md          # Master rules loaded at session start
    ├── skills/            # 42 skills (mega-mind, brainstorming, tech-lead, ...)
    ├── workflows/         # Pre-defined workflow sequences
    ├── agents/            # Persistent agent personas
    └── tests/
        └── run-tests.sh   # Validates the installation
```

### With Copilot (`mega-mind init --copilot`)

```
your-project/
├── .agent/                            # Standard AI tool format (as above)
└── .github/
    ├── copilot-instructions.md        # Global Copilot instructions
    ├── skills/                        # 42 skills as Agent Skills (open standard)
    │   ├── mega-mind/SKILL.md
    │   ├── brainstorming/SKILL.md
    │   ├── tech-lead/SKILL.md
    │   └── ... (39 more)
    └── agents/                        # Custom agent personas
        ├── code-reviewer.agent.md
        ├── tech-lead.agent.md
        └── qa-engineer.agent.md
```

---

## Step 3 — Verify the installation

```bash
bash .agent/tests/run-tests.sh
```

A successful run confirms all skills, workflows, and agents are in place.

---

## Step 4 — Use in GitHub Copilot (VS Code)

After `mega-mind init --copilot`, open VS Code with GitHub Copilot enabled.

In the Copilot Chat:

1. **Use skills as slash commands** — type `/` to see all 42 skills listed
2. **Invoke mega-mind** — type `/mega-mind` to start the orchestrator
3. **Direct skill commands** — type `/brainstorming`, `/tech-lead`, `/debug`, etc.

Skills use Copilot's **progressive disclosure** system:

- Copilot reads `name` + `description` upfront (lightweight)
- Full instructions load only when the skill is relevant to your request
- You can force-invoke any skill with its `/` slash command

---

## Usage (all tools)

Once installed, use the `/mega-mind` command in your AI assistant chat to start orchestrating:

```
/mega-mind help
/mega-mind route I need to add OAuth authentication
/mega-mind route fix the login bug
```

See the full [README](./README.md) for the complete command reference and skill routing matrix.
