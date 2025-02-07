from src.timetrialcomp.competition.infrastructure.dependency_injection import current_competitions_finder
from src.timetrialcomp.shared.presenter import render_timestamp


def present_find_all() -> str:
    current_competitions = list(current_competitions_finder.find_current_competitions())
    return present_competitions(current_competitions)


def present_competitions(current_competitions) -> str:
    if len(current_competitions) == 0:
        return "```No competitions found.```"
    else:
        view_comps = ""
        for comp in current_competitions:
            view_comps += (
                f"🆔: {comp.id}\n"
                f"🏁 Track: {comp.track_code}\n"
                f"🍄 Mode: {comp.mode}\n"
                f"📅 Starts at {render_timestamp(comp.starts_at)}\n"
                f"📅 Ends at {render_timestamp(comp.ends_at)}\n\n"
            )

        return f"```{view_comps}```"
