from src.DomainError import DomainError
from src.Random import Random
from src.TrackRepository import TrackRepository


class SampleSizeExceedsMaxTracksSize(DomainError):
    pass


class SampleSizeShouldBeGreater(DomainError):
    pass


class RandomTracksSampler:

    def __init__(self, tracks_repository: TrackRepository, random: Random) -> None:
        super().__init__()
        self._tracks_repository = tracks_repository
        self._random = random

    def randomize(self, sample_size) -> str:
        if sample_size <= 0:
            raise SampleSizeShouldBeGreater

        tracks_count = self._tracks_repository.count_all()
        if sample_size > tracks_count:
            raise SampleSizeExceedsMaxTracksSize

        tracks = self._tracks_repository.find_all()
        response = f"Listing {sample_size} tracks:\n"
        random_sample = self._random.sample(range(1, tracks_count + 1), sample_size)
        for number in sorted(random_sample):
            response += f'{number}: {tracks.get(number)}\n'

        return response
