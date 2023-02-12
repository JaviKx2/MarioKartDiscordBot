import disnake
from disnake.ext import commands

from src.mkleaderboards.commands.MKLeaderboardsCommand import leaderboards
from src.random.commands.RandomizeCommand import randomize
from src.timetrialcomp.commands.TimeTrialCompetitionCommand import timetrial_competition

bot = commands.InteractionBot()


# noinspection PyTypeChecker
bot.add_slash_command(randomize)
# noinspection PyTypeChecker
bot.add_slash_command(leaderboards)
# noinspection PyTypeChecker
bot.add_slash_command(timetrial_competition)


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="_help"))
    print("Local Bot is ready!")
