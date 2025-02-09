import uuid

from disnake import CommandInteraction
from disnake.ext import commands
from disnake.ext.commands import slash_command

from src.timetrialcomp.competition.domain.timetrial_competition import CreateParams
from src.timetrialcomp.competition.infrastructure.dependency_injection import current_competitions_finder
from src.timetrialcomp.presenter.create import present_create
from src.timetrialcomp.presenter.find_all import present_find_all, present_competition, present_competitions
from src.timetrialcomp.presenter.ranking import present_ranking
from src.timetrialcomp.presenter.submit_time import present_submit_time
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams
from src.timetrialcomp.ui import TTCompView


@slash_command()
async def timetrial_competition(ctx: CommandInteraction):
    pass


@timetrial_competition.sub_command()
async def create(
        ctx: CommandInteraction,
        track: str = commands.Param(description="track code"),
        mode: str = commands.Param(description="mode", choices=["3-Shrooms", "Shroomless"]),
        duration: str = "P1W"
):
    params = CreateParams(id=uuid.uuid4(), track_code=track, mode=mode, duration_iso8601=duration)
    await ctx.send(present_create(params))


@timetrial_competition.sub_command()
async def current(ctx: CommandInteraction):
    await ctx.send(present_find_all())


@timetrial_competition.sub_command()
async def submit_time(
        ctx: CommandInteraction,
        ttcomp_id,
        time,
        pic_url=None,
        ctgp_url=None
):
    params = SubmitTimeParams(
        time=time,
        pic_url=pic_url,
        ctgp_url=ctgp_url,
        timetrial_competition_id=ttcomp_id,
        player_id=str(ctx.user.id)
    )

    await ctx.send(present_submit_time(params))


@timetrial_competition.sub_command()
async def ranking(
        ctx: CommandInteraction,
        ttcomp_id
):
    await ctx.send(await present_ranking(ttcomp_id, ctx.bot.get_user))


@timetrial_competition.sub_command()
async def ui(
        ctx: CommandInteraction
):
    current_competitions = list(current_competitions_finder.find_current_competitions())

    if len(current_competitions) > 0:
        comp = current_competitions[0]
        return await ctx.send(present_competition(comp), view=TTCompView(comp.id))

    await ctx.send(present_competitions(current_competitions))
