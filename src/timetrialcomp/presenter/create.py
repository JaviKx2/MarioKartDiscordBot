from src.shared.domain.errors import has_errors
from src.timetrialcomp.competition.domain.timetrial_competition import CreateParams
from src.timetrialcomp.competition.infrastructure.dependency_injection import timetrial_competition_creator
from src.timetrialcomp.shared.presenter import render_error_message


def present_create(params: CreateParams) -> str:
    created_comp = timetrial_competition_creator.create(params)

    if has_errors(created_comp):
        return render_error_message(created_comp)

    return (
        f"```"
        f"TT Competition was created."
        f"```"
        f"🆔 {created_comp.id}\n"
        f"🍄 {created_comp.mode}\n"
        f"🏁 {created_comp.track_code}\n"
        f"📅 Starts at <t:{created_comp.starts_at.timestamp()}>\n"
        f"📅 Ends at <t:{created_comp.ends_at.timestamp()}>\n"
    )
