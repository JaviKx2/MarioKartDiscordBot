from src.Random import Random


class SampleSizeCalcFactory:
    @staticmethod
    def get(*randomize_args):
        print(randomize_args)
        if len(randomize_args) == 0:
            return RandomSampleSizeCalc(Random())
        if len(randomize_args) == 1:
            return SameSampleSizeCalc(int(randomize_args[0]))
        sample_size_min = int(randomize_args[0])
        sample_size_max = int(randomize_args[1])
        return WithinRangeSampleSizeCalc(Random(), sample_size_min, sample_size_max)


class SampleSizeCalc:
    def calc(self) -> int:
        pass


class SameSampleSizeCalc(SampleSizeCalc):

    def __init__(self, sample_size: int) -> None:
        self._sample_size = sample_size

    def calc(self) -> int:
        return self._sample_size


class WithinRangeSampleSizeCalc(SampleSizeCalc):
    def __init__(self, random: Random, sample_size_min: int, sample_size_max: int) -> None:
        self._random = random
        self.sample_size_min = sample_size_min
        self.sample_size_max = sample_size_max

    def calc(self) -> int:
        return self._random.sample_one(range(self.sample_size_min, self.sample_size_max + 1))


class RandomSampleSizeCalc(SampleSizeCalc):

    def __init__(self, random: Random) -> None:
        self._random = random

    def calc(self) -> int:
        return self._random.sample_one(range(1, 33))
