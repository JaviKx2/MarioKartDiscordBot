import discord
from discord.ext import commands

from src.RandomizeCommand import randomize

bot = commands.Bot(
    intents=discord.Intents.default(),
    command_prefix='^',
    description="Limitless features for Mario Kart games"
)

# noinspection PyTypeChecker
bot.add_command(randomize)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print("Bot is ready!")
