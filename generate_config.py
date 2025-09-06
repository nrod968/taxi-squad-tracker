# generate_config.py
from pathlib import Path

CONFIG_TEMPLATE = """\
# ================================
# Project Information
# ================================
project:
  name: MyProject
  version: 0.1.0
  description: ""
  debug: true  # enable debug mode

# ================================
# Paths
# ================================
paths:
  base_dir: ./                 # project root
  logs_dir: ./logs

# ================================
# Logging
# ================================
logging:
  level: INFO       # DEBUG, INFO, WARNING, ERROR, CRITICAL
  file: ./logs/app.log
  format: "[%(asctime)s] %(levelname)s - %(message)s"

# ================================
# ESPN API Configuration
# ================================

espn_api:
  league_id: 123456789       # replace with your league ID
  year: 2025                 # replace with your league year
  swid: "{YOUR_SWID}"        # replace with your SWID
  espn_s2: "{YOUR_ESPN_S2}"  # replace with your ESPN_S2
"""


def generate_config(path="config.yml"):
    config_path = Path(path)
    if config_path.exists():
        print(f"{path} already exists. Skipping generation.")
        return

    with open(config_path, "w") as f:
        f.write(CONFIG_TEMPLATE)

    print(f"{path} has been created successfully!")


if __name__ == "__main__":
    generate_config()
