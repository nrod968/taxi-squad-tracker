from espn_api.football import League  # type: ignore


def get_roster_size(league: League) -> int:
    return sum(league.settings.position_slot_counts.values())


def number_of_ir_slots(league: League) -> int:
    return league.settings.position_slot_counts["IR"]
