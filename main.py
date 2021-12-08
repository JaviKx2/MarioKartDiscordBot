import os

import discord
from discord.ext import commands

from src.InMemoryTrackRepository import InMemoryTrackRepository
from src.RandomTracksSampler import RandomTracksSampler, SampleSizeExceedsMaxTracksSize, SampleSizeShouldBeGreater

bot = commands.Bot(
    command_prefix='^',
    description="Limitless features for Mario Kart games"
)


@bot.command()
async def randomize(ctx, count: int):
    response = RandomTracksSampler(InMemoryTrackRepository()).randomize(count)
    await ctx.send(response)


@randomize.error
async def randomize_error_handling(ctx, error):
    if isinstance(error.original, SampleSizeShouldBeGreater):
        return await ctx.send("Are u kidding me? Type a number greater than 0.")
    if isinstance(error.original, SampleSizeExceedsMaxTracksSize):
        return await ctx.send("Requested sample size exceeds current tracks size.")
    await ctx.send("Unexpected error occured. Try again later.")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print("Bot is ready!")


bot.run(os.getenv('MARIOKART_BOT_TOKEN'))
