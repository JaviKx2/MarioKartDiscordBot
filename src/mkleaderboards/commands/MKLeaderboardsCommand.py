from disnake import CommandInteraction
from disnake.ext.commands import slash_command

from src.mkleaderboards.commands.CoursesSubcommand import execute as courses_execute


@slash_command()
async def leaderboards(ctx: CommandInteraction):
    pass


@leaderboards.sub_command()
async def courses(ctx: CommandInteraction, track_abbrev: str):
    await courses_execute(ctx, track_abbrev)
