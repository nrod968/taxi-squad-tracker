from pathlib import Path
import yaml


class Config:
    """Recursively convert dicts into nested objects with dot notation."""

    def __init__(self, d):
        for k, v in d.items():
            if isinstance(v, dict):
                v = Config(v)
            setattr(self, k, v)


_config = None


def load_config(path: str = "config.yml") -> Config:
    """Load YAML config into nested object. Only loads once."""
    global _config
    if _config is None:
        config_path = Path(path)
        if not config_path.exists():
            raise FileNotFoundError(f"{path} not found. Generate it first.")
        with open(config_path) as f:
            data = yaml.safe_load(f)
        _config = Config(data)
    return _config


# Load automatically on import
config = load_config()
