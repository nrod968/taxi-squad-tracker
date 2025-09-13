from .league_utils import get_roster_size, number_of_ir_slots
from collections.abc import Iterable
from espn_api.football import League, Team  # type: ignore


def track(taxi_players: Iterable[str], league: League) -> None:
    teams_without_taxi = list(range(1, len(league.teams) + 1))
    for team in league.teams:
        for player in team.roster:
            if player.name in taxi_players:
                print(f"Tracking player: {player.name}")
                print(
                    f"Name: {player.name}, ID: {player.playerId}, Lineup Slot: {player.lineupSlot}, On Team: {player.onTeamId}"
                )
                teams_without_taxi.remove(player.onTeamId)
                check_player_status(player)

    for team_id in teams_without_taxi:
        roster_size = get_roster_size(league)
        ir_slots = number_of_ir_slots(league)
        team = league.teams[team_id - 1]  # team IDs are 1-based, list is 0-based
        enforce_bench_rule(team, roster_size, ir_slots)


def check_player_status(player) -> None:
    if not player.lineupSlot == "BE":
        print(
            f"Player {player.name} is not on the bench. Current slot: {player.lineupSlot}"
        )
        print("Please move the player to the bench to comply with taxi squad rules.")
    else:
        print(f"Player {player.name} is correctly placed on the bench.")


def enforce_bench_rule(team: Team, roster_size: int, ir_slots: int) -> None:
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
    else:
        print(
            f"Team {team.team_name} (ID: {team.team_id}) is in compliance with taxi squad rules."
        )
