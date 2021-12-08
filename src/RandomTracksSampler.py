import random

from src.DomainError import DomainError


class SampleSizeExceedsMaxTracksSize(DomainError):
    pass


class SampleSizeShouldBeGreater(DomainError):
    pass


class RandomTracksSampler:

    def __init__(self, tracks_repository) -> None:
        super().__init__()
        self.tracks_repository = tracks_repository

    def randomize(self, sample_size: int) -> str:
        if sample_size <= 0:
            raise SampleSizeShouldBeGreater
        tracks_count = self.tracks_repository.count_all()
        if sample_size > tracks_count:
            raise SampleSizeExceedsMaxTracksSize
        tracks = self.tracks_repository.find_all()
        response = f"Listing {sample_size} randomized tracks:\n"
        random_sample = random.sample(range(1, tracks_count + 1), sample_size)
        for number in sorted(random_sample):
            response += f'{number}: {tracks.get(number)}\n'
        return response
