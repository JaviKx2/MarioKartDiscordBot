from src.Random import Random


class SampleSizeCalcFactory:
    @staticmethod
    def get(randomize_args):
        if len(randomize_args) == 0:
            return RandomSampleSizeCalc(Random())
        if len(randomize_args) == 1:
            return SameSampleSizeCalc(int(randomize_args[0]))
        sample_size_min = int(randomize_args[0])
        sample_size_max = int(randomize_args[1])
        return WithinRangeSampleSizeCalc(Random(), sample_size_min, sample_size_max)


class SampleSizeCalc:
    def calc(self, max_size: int) -> int:
        pass


class SameSampleSizeCalc(SampleSizeCalc):

    def __init__(self, sample_size: int) -> None:
        self._sample_size = sample_size

    def calc(self, max_size: int) -> int:
        return self._sample_size if self._sample_size < max_size else max_size


class WithinRangeSampleSizeCalc(SampleSizeCalc):
    def __init__(self, random: Random, sample_lower_limit: int, sample_upper_limit: int) -> None:
        self._random = random
        self._sample_lower_limit = sample_lower_limit
        self._sample_upper_limit = sample_upper_limit

    def calc(self, max_size: int) -> int:
        sample_upper_limit = max_size if max_size < self._sample_upper_limit else self._sample_upper_limit
        return self._random.sample_one(range(self._sample_lower_limit, sample_upper_limit + 1))


class RandomSampleSizeCalc(SampleSizeCalc):

    def __init__(self, random: Random) -> None:
        self._random = random

    def calc(self, max_size: int) -> int:
        return self._random.sample_one(range(1, max_size + 1))
