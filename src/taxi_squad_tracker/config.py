from pathlib import Path

import yaml


class Config:
    """Recursively convert dicts into nested objects with dot notation."""

    def __init__(self, item: dict):
        self.config_builder(item)

    def config_builder(self, dictionary: dict):
        if len(dictionary) == 0:
            return

        key = list(dictionary.keys())[0]
        value = dictionary.pop(key)
        if isinstance(value, dict):
            value = Config(value)
        if isinstance(value, list):
            value = self.config_list_builder(value)

        setattr(self, key, value)
        self.config_builder(dictionary)

    def config_list_builder(self, input_list: list) -> list:
        if len(input_list) == 0:
            return []

        item = input_list.pop()
        if isinstance(item, dict):
            item = Config(item)
        elif isinstance(item, list):
            item = self.config_list_builder(item)

        return self.config_list_builder(input_list) + [item]

    def __getattr__(self, name: str):
        return self.__dict__.get(name)


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
        if not isinstance(data, dict):
            raise TypeError("Config file must be a dict at top level")
        _config = Config(data)
    return _config


# Load automatically on import
config = load_config()
