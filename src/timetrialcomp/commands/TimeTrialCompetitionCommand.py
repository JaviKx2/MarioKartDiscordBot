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
async def create(
        ctx: CommandInteraction,
        track: str = commands.Param(description="track code"),
        mode: str = commands.Param(description="mode", choices=["3-Schrooms", "Shroomless"]),
        duration: str = "P1W"
):
    print(ctx.user)
    created_comp = timetrial_competition_creator.create(
        CreateParams(
            id=uuid.uuid4(),
            track_code=track,
            mode=mode,
            duration_iso8601=duration
        )
    )

    if has_errors(created_comp):
        error: DomainError = created_comp
        return await ctx.send("ERROR: " + error.message)

    await ctx.send(
        f"TT Competition was created.\n\n"
        f"🆔: {created_comp.id}\n"
        f"🏁 Mode: {created_comp.mode}\n"
        f"🏁 Track: {created_comp.track_code}\n"
        f"📅 Starts at <t:{created_comp.starts_at.timestamp()}>\n"
        f"📅 Ends at <t:{created_comp.ends_at.timestamp()}>\n"
    )


@timetrial_competition.sub_command()
async def current(ctx: CommandInteraction):
    current_competitions = list(current_competitions_finder.find_current_competitions())

    if len(current_competitions) == 0:
        await ctx.send(f"No competitions found.")
    else:
        view_comps = ""
        for comp in current_competitions:
            view_comps += (
                f"🆔: {comp.id}\n"
                f"🏁 Track: {comp.track_code}\n"
                f"🍄 Mode: {comp.mode}\n"
                f"📅 Starts at <t:{str(comp.starts_at.timestamp()).split(".")[0]}>\n"
                f"📅 Ends at <t:{str(comp.ends_at.timestamp()).split(".")[0]}>\n\n"
            )

        await ctx.send(
            f"Current competitions:\n\n"
            f"{view_comps}"
        )


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

    submitted_time = time_submitter.submit_time(params)

    if has_errors(submitted_time):
        error: DomainError = submitted_time
        return await ctx.send("ERROR: " + error.message)

    await ctx.send("Time was submitted.")


@timetrial_competition.sub_command()
async def ranking(
        ctx: CommandInteraction,
        ttcomp_id
):
    ranking_response = time_submitter.ranking(ttcomp_id)

    if has_errors(ranking_response):
        error: DomainError = ranking_response
        return await ctx.send("ERROR: " + error.message)

    view_rows = ""
    for i, row in enumerate(ranking_response):
        view_rows += (
            f"{i+1}. "
            f"Name: <@{ctx.user.id}>\t"
            f"🕒 Time: {row['time']}\t"
            f"📸 Pic: {row['pic_url']}\t"
            f"🔗 CTGP: {row['ctgp_url']}\t"
            f"Approved: {'✔' if row['approved'] else '❌'}\n"
        )

    await ctx.send(
        f"Ranking:\n\n{view_rows}"
    )
