import click
import sys
from .installer import install_skills


@click.group()
@click.version_option(package_name="mega-mind-orchestrator")
def cli():
    """Mega-Mind Orchestrator CLI"""
    pass


@cli.command()
@click.argument("target_dir", type=click.Path(), default=".")
@click.option("--force", "-f", is_flag=True, help="Overwrite existing files")
@click.option(
    "--copilot",
    is_flag=True,
    help="Also install GitHub Copilot-compatible files into .github/",
)
def init(target_dir, force, copilot):
    """Initialize Mega-Mind skills in the target directory.

    By default, installs to .agent/ for Antigravity / Claude / standard agent tools.

    Use --copilot to also install into .github/ for GitHub Copilot (VS Code).
    This creates .github/copilot-instructions.md, .github/skills/, and .github/agents/.
    """
    try:
        install_skills(target_dir, force, copilot)
        click.echo(
            click.style(
                f" ✅ Successfully initialized Mega-Mind in {target_dir}",
                fg="green",
            )
        )
        if copilot:
            click.echo(
                click.style(
                    "    🤖 GitHub Copilot files installed in .github/",
                    fg="cyan",
                )
            )
            click.echo(
                click.style(
                    "    📂 Skills available as slash commands in VS Code Copilot chat",
                    fg="cyan",
                )
            )
    except Exception as e:
        click.echo(click.style(f" ❌ Error: {str(e)}", fg="red"), err=True)
        sys.exit(1)


def main():
    cli()


if __name__ == "__main__":
    main()
