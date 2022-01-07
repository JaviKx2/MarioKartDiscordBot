from discord.ext.commands import command

from src.InMemoryTrackRepository import InMemoryTrackRepository
from src.Random import Random
from src.RandomTracksSampler import RandomTracksSampler, SampleSizeShouldBeGreater, \
    SampleSizeExceedsMaxTracksSize
from src.SampleSizeCalc import SampleSizeCalcFactory


@command(aliases=["r", "rand"])
async def randomize(ctx, *args):
    sampler = RandomTracksSampler(InMemoryTrackRepository(), Random())
    sample_size_calc = SampleSizeCalcFactory.get(*args)
    response = sampler.randomize(sample_size_calc.calc())
    await ctx.send(response)


@randomize.error
async def randomize_error_handling(ctx, error):
    if isinstance(error.original, SampleSizeShouldBeGreater):
        return await ctx.send("Are u kidding me? Type a number greater than 0.")
    if isinstance(error.original, SampleSizeExceedsMaxTracksSize):
        return await ctx.send("Requested sample size exceeds current tracks size.")
    await ctx.send("Unexpected error occured. Try again later.")
