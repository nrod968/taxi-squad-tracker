from collections.abc import Iterable

from espn_api.football import League, Player, Team  # type: ignore

# Replace most of this with a DB
from .config import config
from .league_utils import get_roster_size, number_of_ir_slots
from .smtp import send_sms_via_email


def track(taxi_player_names: Iterable[str], league: League) -> None:
    teams_without_taxi = league.teams.copy()
    taxi_players = []
    for team in league.teams:
        for player in team.roster:
            if player.name in taxi_player_names:
                print(f"Tracking player: {player.name}")
                print(
                    f"Name: {player.name}, ID: {player.playerId}, Lineup Slot: {player.lineupSlot}, On Team: {player.onTeamId}"
                )
                teams_without_taxi.remove(team)
                taxi_players.append(player)

    roster_size = get_roster_size(league)
    ir_slots = number_of_ir_slots(league)
    enforce_taxi_rules(teams_without_taxi, taxi_players, roster_size, ir_slots)


def enforce_taxi_rules(
    teams_without_taxi: Iterable[Team],
    taxi_players: Iterable[Player],
    roster_size: int,
    ir_slots: int,
) -> None:
    for player in taxi_players:
        if not check_player_status(player):
            team_id = player.onTeamId
            team_config = config.smtp.team_info[team_id - 1]
            send_sms_via_email(
                team_config.email,
                f"Are you sure you want to activate {player.name} from your Taxi Squad? You will lose their bench spot for the rest of the season.",
            )

    for team in teams_without_taxi:
        check_roster_validity(team, roster_size, ir_slots)
        team_id = team.team_id
        team_config = config.smtp.team_info[team_id - 1]
        # commissioner_config = config.smtp.team_info[0]

        send_sms_via_email(
            team_config.email,
            "Your team has no taxi spot, please drop a player within the next 2 hours before the commissioner is forced to take action.",
        )
        # send_sms_via_email(commissioner_config.phone_number, commissioner_config.sms_gateway, f"Just a heads up. {team.team_name} has no taxi squad spot and has too many players on their roster. They have been notified.")


def check_player_status(player: Player) -> bool:
    if not player.lineupSlot == "BE":
        print(
            f"Player {player.name} is not on the bench. Current slot: {player.lineupSlot}"
        )
        print("Please move the player to the bench to comply with taxi squad rules.")
        return False
    else:
        print(f"Player {player.name} is correctly placed on the bench.")
        return True


def check_roster_validity(team: Team, roster_size: int, ir_slots: int) -> bool:
    core_roster_slots = roster_size - ir_slots
    allowable_roster_size = core_roster_slots - 1
    core_roster_slots_in_use = len(
        [player for player in team.roster if player.lineupSlot != "IR"]
    )

    if core_roster_slots_in_use > allowable_roster_size:
        print(
            f"Team {team.team_name} (ID: {team.team_id}) has no taxi spot and must leave one bench spot open."
        )
        print(
            f"Roster slots in use (not including IR): {core_roster_slots_in_use}, Allowable roster size (not including IR): {allowable_roster_size}"
        )
        print("Please adjust your roster to comply with taxi squad rules.")

        return False
    else:
        print(
            f"Team {team.team_name} (ID: {team.team_id}) is in compliance with taxi squad rules."
        )
        return True
