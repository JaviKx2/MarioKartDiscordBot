from discord.ext.commands import command

from src.InMemoryTrackRepository import InMemoryTrackRepository
from src.Random import Random
from src.RandomTracksSampler import RandomTracksSampler, SampleSizeShouldBeGreater, \
    SampleSizeExceedsMaxTracksSize
from src.SampleSizeCalc import SampleSizeCalcFactory

sampler = RandomTracksSampler(InMemoryTrackRepository(), Random())


@command(aliases=["r", "rand"])
async def randomize(ctx, *args):
    sample_size_calc = SampleSizeCalcFactory.get(*args)
    response = sampler.randomize(sample_size_calc.calc())
    await ctx.send(response)


@randomize.error
async def handle_randomize_errors(ctx, error):
    if isinstance(error.original, SampleSizeShouldBeGreater):
        return await ctx.send("Are u kidding me? Type a number greater than 0.")
    if isinstance(error.original, SampleSizeExceedsMaxTracksSize):
        return await ctx.send("Requested sample size exceeds current tracks size.")
    await ctx.send("Unexpected error occured. Try again later.")


@randomize.after_invoke
async def after_invoke(ctx):
    await ctx.send("Here you go!")


@randomize.before_invoke
async def before_invoke(ctx):
    await ctx.send("Randomizing...")
