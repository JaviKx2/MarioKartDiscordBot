from disnake import CommandInteraction
from disnake.ext.commands import slash_command

from src.InMemoryTrackRepository import InMemoryTrackRepository
from src.Random import Random
from src.RandomTracksSampler import RandomTracksSampler, SampleSizeShouldBeGreater, \
    SampleSizeExceedsMaxTracksSize
from src.SampleSizeCalc import SampleSizeCalcFactory, RandomSampleSizeCalc, WithinRangeSampleSizeCalc

tracks_repository = InMemoryTrackRepository()
sampler = RandomTracksSampler(tracks_repository, Random())

help_message = '^randomize: Returns a list of tracks with a random size\t' \
               '^randomize {number}: Returns  a list with {number} tracks\t' \
               '^randomize {number} {number}: Returns a list of tracks with a size between the numbers provided'


@slash_command(
    name="track_sampler",
    description="Use this command to get track samples"
)
async def randomize(ctx: CommandInteraction):
    pass


@randomize.sub_command(
    description="List tracks within a range"
)
async def sample_range(ctx: CommandInteraction, start: int, end: int):
    max_size = tracks_repository.count_all()
    sample_size = WithinRangeSampleSizeCalc(Random(), start, end).calc(max_size)
    response = sampler.randomize(sample_size)
    await ctx.send(response)


@randomize.sub_command(
    description="List tracks with a concrete size"
)
async def size(ctx: CommandInteraction, sample_size: int):
    response = sampler.randomize(sample_size)
    await ctx.send(response)


@randomize.sub_command(
    description="List tracks with random size"
)
async def random_size(ctx: CommandInteraction):
    max_size = tracks_repository.count_all()
    sample_size = RandomSampleSizeCalc(Random()).calc(max_size)
    response = sampler.randomize(sample_size)
    await ctx.send(response)


@randomize.error
async def handle_randomize_errors(ctx: CommandInteraction, error):
    if isinstance(error.original, SampleSizeShouldBeGreater):
        return await ctx.send("Are u kidding me? Type a number greater than 0.")
    if isinstance(error.original, SampleSizeExceedsMaxTracksSize):
        return await ctx.send("Requested sample size exceeds current tracks size.")
    await ctx.send("Unexpected error occured. Try again later.")


def register(bot):
    bot.add_slash_command(randomize)
