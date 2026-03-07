import shutil
from pathlib import Path


def install_skills(target_dir: str, force: bool = False):
    """Copies assets to the target .agent directory."""
    target_path = Path(target_dir).resolve()
    agent_path = target_path / ".agent"

    # Discovery of assets embedded in the package
    # We use pkgutil or simply relative path if we know the structure
    assets_src = Path(__file__).parent / "assets"

    if not assets_src.exists():
        raise FileNotFoundError(f"Source assets not found at {assets_src}")

    if agent_path.exists() and not force:
        raise FileExistsError(
            f".agent directory already exists in {target_dir}. Use --force to overwrite."
        )

    # For now, we manually copy if assets_src exists
    # In a real wheel, we might need pkg_resources/importlib.resources
    shutil.copytree(assets_src, agent_path, dirs_exist_ok=True)
