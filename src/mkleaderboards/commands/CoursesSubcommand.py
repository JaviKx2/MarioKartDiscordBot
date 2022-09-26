from disnake import CommandInteraction

from src.mkleaderboards.MKLeaderboards import get_course


async def execute(ctx: CommandInteraction, track_abbrev: str):
    track = get_course(track_abbrev)
    response = ">>> "
    for player in track.get('data'):
        response += f"{str(player.get('rank')) + '.': <5} {player.get('name'):>10} {player.get('score_formatted'):^20}\n"
    await ctx.send(response)
