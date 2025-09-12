from .config import config
from .league_loader import load_league
from .taxi_squad_tracker import track


def main():
    print("Taxi Squad Tracker")
    print("Config Loaded")

    league = load_league(
        config.espn_api.league_id,
        config.espn_api.year,
        config.espn_api.swid,
        config.espn_api.espn_s2,
    )

    track(config.taxi_squad, league)


if __name__ == "__main__":
    main()
