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

# ================================
# SMTP Email Configuration
# ================================

smtp:
  server: smtp.gmail.com
  port: 587
  email: "{YOUR_GMAIL_ADDRESS}"  # replace with your gmail address
  password: "{YOUR_GMAIL_APP_PASSWORD}"  # replace with your gmail app password
  sms_gateways:
    - "{phone_number}@txt.att.net"                # AT&T
    - "{phone_number}@vtext.com"                  # Verizon
    - "{phone_number}@tmomail.net"                # T-Mobile
    - "{phone_number}@messaging.sprintpcs.com"    # Sprint
    - "{phone_number}@mymetropcs.com"             # MetroPCS
    - "{phone_number}@sms.myboostmobile.com"      # Boost Mobile
    - "{phone_number}@sms.cricketwireless.net"    # Cricket Wireless
    - "{phone_number}@msg.fi.google.com"          # Google Fi
    - "{phone_number}@email.uscc.net"             # US Cellular
    - "{phone_number}@vmobl.com"                  # Virgin Mobile
  team_info:
    - id: 1
      phone_number: 0000000000
      sms_gateway: "{ENTER_SMS_GATEWAY_HERE}"  # replace with your carrier's SMS gateway
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
