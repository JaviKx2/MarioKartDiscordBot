import random


class Random:
    def sample(self, sample_range, sample_size) -> list[int]:
        return random.sample(sample_range, sample_size)
