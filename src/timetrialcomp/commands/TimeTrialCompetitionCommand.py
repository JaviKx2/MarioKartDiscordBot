import uuid
from datetime import datetime

from disnake import CommandInteraction
from disnake.ext import commands
from disnake.ext.commands import slash_command

from src.shared.domain.errors import has_errors, DomainError
from src.timetrialcomp.competition.domain.timetrial_competition import CreateTimeTrialCompetitionParams
from src.timetrialcomp.competition.infrastructure.dependency_injection import timetrial_competition_creator, \
    current_competitions_finder, time_submitter
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams


@slash_command()
async def timetrial_competition(ctx: CommandInteraction):
    pass


@timetrial_competition.sub_command()
async def create(
        ctx: CommandInteraction,
        track: str = commands.Param(description="track code"),
        starts_at=None,
        duration_in_months=None
):
    params = CreateTimeTrialCompetitionParams(
        id=uuid.uuid4(),
        track_code=track,
        starts_at=starts_at,
        duration_in_months=duration_in_months
    )

    create_response = timetrial_competition_creator.create(params)

    if has_errors(create_response):
        error: DomainError = create_response
        return await ctx.send("ERROR: " + error.message)

    await ctx.send("TT Competition was created.")


@timetrial_competition.sub_command()
async def current(ctx: CommandInteraction):
    current_competitions = current_competitions_finder.find_current_competitions()

    await ctx.send(f"Current competition: {current_competitions[0].track}")


@timetrial_competition.sub_command()
async def submit_time(
        ctx: CommandInteraction,
        time,
        pic_url,
        ctgp_url
):
    current_competitions = current_competitions_finder.find_current_competitions()
    first_running_competition = current_competitions[0]
    params = SubmitTimeParams(time=time, pic_url=pic_url, ctgp_url=ctgp_url,
                              timetrial_competition_id=first_running_competition.id)

    submit_time_response = time_submitter.submit_time(params)

    if has_errors(submit_time_response):
        error: DomainError = submit_time_response
        return await ctx.send("ERROR: " + error.message)

    await ctx.send("Time was submitted.")
