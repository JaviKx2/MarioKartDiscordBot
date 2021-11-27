import random

from src.DomainError import DomainError


class NotEnoughTracks(DomainError):
    pass


class RandomTracksSampler:

    def __init__(self, tracks_repository) -> None:
        super().__init__()
        self.tracks_repository = tracks_repository

    def randomize(self, count: int) -> str:
        tracks_count = self.tracks_repository.count_all()
        if count < 0 or count > tracks_count:
            raise NotEnoughTracks
        if count == 0:
            return "Are u kidding me?"
        tracks = self.tracks_repository.find_all()
        response = "Track list:\n"
        random_sample = random.sample(range(1, tracks_count + 1), count)
        for number in sorted(random_sample):
            response += f'{number}: {tracks.get(number)}\n'
        return response
