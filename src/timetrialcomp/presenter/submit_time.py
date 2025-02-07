from src.shared.domain.errors import has_errors
from src.timetrialcomp.competition.infrastructure.dependency_injection import time_submitter
from src.timetrialcomp.shared.presenter import render_error_message
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams


def present_submit_time(params: SubmitTimeParams) -> str:
    submitted_time = time_submitter.submit_time(params)

    if has_errors(submitted_time):
        return render_error_message(submitted_time)

    return "```Time was submitted.```"
