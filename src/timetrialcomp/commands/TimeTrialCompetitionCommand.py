from disnake import CommandInteraction
from disnake.ext.commands import slash_command

from src.mkleaderboards.commands.CoursesSubcommand import execute as courses_execute
from src.mkleaderboards.commands.RankingSubcommand import execute as ranking_execute, RankingScopeChoice


@slash_command()
async def timetrial_competition(ctx: CommandInteraction):
    pass


@timetrial_competition.sub_command()
async def create(ctx: CommandInteraction, **kwargs):
    await courses_execute(ctx, kwargs)


@timetrial_competition.sub_command()
async def current(ctx: CommandInteraction, kwargs):
    await ranking_execute(ctx, kwargs)
