from disnake import CommandInteraction
from disnake.ext.commands import slash_command

from src.MKLeaderboards import get_course


@slash_command()
async def leaderboards(ctx: CommandInteraction, track_abbrev: str):
    track = get_course(track_abbrev)
    response = ">>> "
    for player in track.get('data'):
        response += f"{str(player.get('rank')) + '.': <5} {player.get('name'):>10} {player.get('score_formatted'):^20}\n"
    await ctx.send(response)
