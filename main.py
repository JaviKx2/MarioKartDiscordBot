import discord
from discord.ext import commands
import os

from src.InMemoryTrackRepository import InMemoryTrackRepository
from src.RandomTracksSampler import RandomTracksSampler, NotEnoughTracks

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
    if isinstance(error, NotEnoughTracks):
        await ctx.send("Número no válido. Intente con otro diferente.")
    await ctx.send("Ha ocurrido un error. Inténtalo más tarde.")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print("Bot is ready!")


bot.run(os.getenv('MARIOKART_BOT_TOKEN'))
