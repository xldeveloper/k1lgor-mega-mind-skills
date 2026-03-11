import shutil
from pathlib import Path


def install_skills(
    target_dir: str, force: bool = False, copilot: bool = False, claude: bool = False
):
    """Copies assets to the target .agent directory.

    Args:
        target_dir: The root directory of the project to install into.
        force: If True, overwrite existing files.
        copilot: If True, also install skills into .github/ for GitHub Copilot.
        claude: If True, also install skills into CLAUDE.md and .claude/ for Claude Code.
    """
    target_path = Path(target_dir).resolve()
    agent_path = target_path / ".agent"

    # Discovery of assets embedded in the package
    assets_src = Path(__file__).parent / "assets"

    if not assets_src.exists():
        raise FileNotFoundError(f"Source assets not found at {assets_src}")

    if agent_path.exists() and not force:
        raise FileExistsError(
            f".agent directory already exists in {target_dir}. Use --force to overwrite."
        )

    # Install to .agent/ (Antigravity / Claude / standard agent format)
    shutil.copytree(assets_src, agent_path, dirs_exist_ok=True)

    if copilot:
        _install_github_copilot(assets_src, target_path, force)

    if claude:
        _install_claude_code(assets_src, target_path, force)


def _install_github_copilot(assets_src: Path, target_path: Path, force: bool):
    """Install GitHub Copilot-compatible files into .github/ directory.

    Creates:
      .github/copilot-instructions.md  — global Copilot instructions (from AGENTS.md)
      .github/skills/<name>/SKILL.md   — all 42 skills (Agent Skills standard)
      .github/agents/<name>.agent.md   — all agent personas
    """
    github_path = target_path / ".github"

    # 1. Copy copilot-instructions.md from AGENTS.md
    agents_md = assets_src / "AGENTS.md"
    copilot_instructions = github_path / "copilot-instructions.md"
    if agents_md.exists():
        copilot_instructions.parent.mkdir(parents=True, exist_ok=True)
        if not copilot_instructions.exists() or force:
            shutil.copy2(agents_md, copilot_instructions)

    # 2. Copy skills to .github/skills/<name>/SKILL.md
    skills_src = assets_src / "skills"
    skills_dst = github_path / "skills"
    if skills_src.exists():
        for skill_dir in skills_src.iterdir():
            if skill_dir.is_dir():
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    dest_dir = skills_dst / skill_dir.name
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest_file = dest_dir / "SKILL.md"
                    if not dest_file.exists() or force:
                        shutil.copy2(skill_md, dest_file)

    # 3. Copy agents to .github/agents/<name>.agent.md
    agents_src = assets_src / "agents"
    agents_dst = github_path / "agents"
    if agents_src.exists():
        agents_dst.mkdir(parents=True, exist_ok=True)
        for agent_file in agents_src.iterdir():
            if agent_file.is_file() and agent_file.suffix == ".md":
                # Convert name.md → name.agent.md (GitHub Copilot format)
                new_name = agent_file.stem + ".agent.md"
                dest_file = agents_dst / new_name
                if not dest_file.exists() or force:
                    content = agent_file.read_text(encoding="utf-8")
                    # Add YAML frontmatter if not already present
                    if not content.startswith("---"):
                        lines = content.split("\n")
                        title = next(
                            (
                                line.lstrip("#").strip()
                                for line in lines
                                if line.startswith("#")
                            ),
                            agent_file.stem,
                        )
                        frontmatter = (
                            f"---\n"
                            f"description: {title} - specialized Mega-Mind agent\n"
                            f'tools: ["editFiles", "runCommands", "search", "fetch"]\n'
                            f"---\n\n"
                        )
                        content = frontmatter + content
                    dest_file.write_text(content, encoding="utf-8")


def _install_claude_code(assets_src: Path, target_path: Path, force: bool):
    """Install Claude Code-compatible files.

    Creates:
      CLAUDE.md       — project rules (from AGENTS.md)
      .claude/skills/ — all skills (Agent Skills standard)
    """
    # 1. Create CLAUDE.md in root (mirror of AGENTS.md)
    agents_md = assets_src / "AGENTS.md"
    claude_md = target_path / "CLAUDE.md"
    if agents_md.exists():
        if not claude_md.exists() or force:
            shutil.copy2(agents_md, claude_md)

    # 2. Copy skills to .claude/skills/<name>/SKILL.md
    skills_src = assets_src / "skills"
    claude_skills_dst = target_path / ".claude" / "skills"
    if skills_src.exists():
        for skill_dir in skills_src.iterdir():
            if skill_dir.is_dir():
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    dest_dir = claude_skills_dst / skill_dir.name
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest_file = dest_dir / "SKILL.md"
                    if not dest_file.exists() or force:
                        shutil.copy2(skill_md, dest_file)
