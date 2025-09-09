from .config_loader import config
from espn_api.football import League  # type: ignore


def list_teams(league: League):
    teams = league.teams
    for team in teams:
        print(f"Team: {team.team_name}, ID: {team.team_id}")


def get_player(league: League, player_name: str):
    # Placeholder function to get player details
    print(f"Fetching details for player: {player_name}")
    return league.player_info(player_name)


def taxi_squad_init(league: League):
    print("Initializing Taxi Squad Tracker...")
    taxi_squad = []
    for taxi_player in config.taxi_squad:
        player = get_player(league, taxi_player["name"])
        print(f"Tracking player: {player.name}")
        taxi_squad.append(player)
    return taxi_squad


def main():
    print("Taxi Squad Tracker")
    print("Config Loaded")
    print(f"League ID: {config.espn_api.league_id}")
    print(f"Year: {config.espn_api.year}")
    print(f"Swid: {config.espn_api.swid}")
    print(f"S2: {config.espn_api.espn_s2}")
    league = League(
        league_id=config.espn_api.league_id,
        year=config.espn_api.year,
        swid=config.espn_api.swid,
        espn_s2=config.espn_api.espn_s2,
    )

    list_teams(league)
    taxi_squad = taxi_squad_init(league)
    for player in taxi_squad:
        print(
            f"Name: {player.name}, Position: {player.position}, Team: {player.proTeam}, ID: {player.playerId}"
        )
        print(f"Injury Status: {player.injuryStatus}")
        print(f"Acquisition Type: {player.acquisitionType}")
        print(f"On Team: {player.onTeamId}")


if __name__ == "__main__":
    main()
