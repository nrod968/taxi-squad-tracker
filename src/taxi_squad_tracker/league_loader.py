from espn_api.football import League  # type: ignore

_leagues: dict[int, League] = {}


def load_league(
    league_id: int, year: int, swid: str | None, espn_s2: str | None
) -> League:
    """Load the league using given settings. Only loads once."""
    global _leagues
    if league_id not in _leagues.keys():
        league = League(league_id, year, espn_s2, swid)
        _leagues[league_id] = league
    else:
        league = _leagues[league_id]
    return league
