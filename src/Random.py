import random


class Random:
    def sample(self, sample_range, sample_size) -> list[int]:
        return random.sample(sample_range, sample_size)

    def sample_one(self, sample_range) -> int:
        return random.sample(sample_range, 1)[0]
