from disnake import CommandInteraction
from disnake.ext.commands import slash_command

from src.mkleaderboards.commands.CoursesSubcommand import execute as courses_execute
from src.mkleaderboards.commands.RankingSubcommand import execute as ranking_execute, RankingScopeChoice


@slash_command()
async def leaderboards(ctx: CommandInteraction):
    pass


@leaderboards.sub_command()
async def courses(ctx: CommandInteraction, track_abbrev: str):
    await courses_execute(ctx, track_abbrev)


@leaderboards.sub_command()
async def ranking(ctx: CommandInteraction, scope: RankingScopeChoice):
    await ranking_execute(ctx, scope)


def register(bot):
    bot.add_slash_command(leaderboards)
