import uuid

from disnake import CommandInteraction
from disnake.ext import commands
from disnake.ext.commands import slash_command

from src.shared.domain.errors import has_errors, DomainError
from src.timetrialcomp.competition.domain.timetrial_competition import CreateParams
from src.timetrialcomp.competition.infrastructure.dependency_injection import timetrial_competition_creator, \
    current_competitions_finder, time_submitter
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams


@slash_command()
async def timetrial_competition(ctx: CommandInteraction):
    pass


@timetrial_competition.sub_command()
@commands.has_permissions(administrator=True)
async def create(
        ctx: CommandInteraction,
        track: str = commands.Param(description="track code"),
        starts_at=None,
        duration_in_months=None
):
    create_response = timetrial_competition_creator.create(
        CreateParams(
            id=uuid.uuid4(),
            track_code=track,
            starts_at=starts_at,
            duration_in_months=duration_in_months
        )
    )

    if has_errors(create_response):
        error: DomainError = create_response
        return await ctx.send("ERROR: " + error.message)

    await ctx.send(f"TT Competition was created.\n\n"
                   f"🆔: {create_response.id}\n"
                   f"🏁 Track: {create_response.track_code}\n"
                   f"📅 Starts at {create_response.starts_at}\n"
                   f"📅 Ends at {create_response.ends_at}\n")


@timetrial_competition.sub_command()
async def current(ctx: CommandInteraction):
    current_competitions = current_competitions_finder.find_current_competitions()

    if len(current_competitions) == 0:
        await ctx.send(f"No competitions found.")
    else:
        await ctx.send(f"Current competition: {current_competitions[0].track}")


@timetrial_competition.sub_command()
async def submit_time(
        ctx: CommandInteraction,
        ttcomp_id,
        time,
        pic_url,
        ctgp_url
):
    params = SubmitTimeParams(time=time, pic_url=pic_url, ctgp_url=ctgp_url,
                              timetrial_competition_id=ttcomp_id)

    submit_time_response = time_submitter.submit_time(params)

    if has_errors(submit_time_response):
        error: DomainError = submit_time_response
        return await ctx.send("ERROR: " + error.message)

    await ctx.send("Time was submitted.")
