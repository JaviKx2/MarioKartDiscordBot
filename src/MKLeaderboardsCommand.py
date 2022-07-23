from discord.ext.commands import command, Context

from src.MKLeaderboards import get_course


@command(
    aliases=["l", "lb"],
    help="Leaderboards"
)
async def leaderboards(ctx: Context, *args):
    print(ctx.author.id)
    print(ctx.author.name)
    print(ctx.message)
    print(ctx.channel)
    print(ctx.guild)
    print(ctx.me)
    track = get_course(args[0])
    response = ">>> "
    for player in track.get('data'):
        response += f"{str(player.get('rank')) + '.': <5} {player.get('name'):>10} {player.get('score_formatted'):^20}\n"
    await ctx.send(response)


@leaderboards.after_invoke
async def after_invoke(ctx: Context):
    await ctx.send(f"<@{ctx.author.id}>, results are ready!", reference=ctx.message)

