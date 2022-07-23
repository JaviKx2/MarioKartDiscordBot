import discord
from discord.ext import commands

from src.MKLeaderboardsCommand import leaderboards
from src.RandomizeCommand import randomize

bot = commands.Bot(
    command_prefix='^',
    description="Limitless features for Mario Kart games"
)

# noinspection PyTypeChecker
bot.add_command(randomize)
# noinspection PyTypeChecker
bot.add_command(leaderboards)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print("Local Bot is ready!")
