import disnake
from disnake.ext import commands

from src.mkleaderboards.commands.MKLeaderboardsCommand import leaderboards
from src.RandomizeCommand import randomize

bot = commands.InteractionBot()


# noinspection PyTypeChecker
bot.add_slash_command(randomize)
# noinspection PyTypeChecker
bot.add_slash_command(leaderboards)


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="_help"))
    print("Local Bot is ready!")
