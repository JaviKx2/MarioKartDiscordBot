from unittest import TestCase

from src.Random import Random
from src.RandomTracksSampler import RandomTracksSampler, SampleSizeShouldBeGreater, SampleSizeExceedsMaxTracksSize
from src.TrackRepository import TrackRepository


class MockTrackRepository(TrackRepository):

    def count_all(self) -> int:
        return 32

    def find_all(self) -> dict:
        return {
            1: 'Luigi Circuit',
            2: 'Moo Moo Meadows',
            3: 'Mushroom Gorge',
            4: 'Toad\'s Factory',
            5: 'Mario Circuit',
            6: 'Coconut Mall',
            7: 'DK Summit',
            8: 'Wario\'s Gold Mine',
            9: 'Daisy Circuit',
            10: 'Koopa Cape',
            11: 'Maple Treeway',
            12: 'Grumble Volcano',
            13: 'Dry Dry Ruins',
            14: 'Moonview Highway',
            15: 'Bowser\'s Castle',
            16: 'Rainbow Road',
            17: 'GCN Peach Beach',
            18: 'DS Yoshi Falls',
            19: 'SNES Ghost Valley 2',
            20: 'N64 Mario Raceway',
            21: 'N64 Sherbet Land',
            22: 'GBA Shy Guy Beach',
            23: 'DS Delfino Square',
            24: 'GCN Waluigi Stadium',
            25: 'DS Desert Hills',
            26: 'GBA Bowser Castle 3',
            27: 'N64 DK\'s Jungle Parkway',
            28: 'GCN Mario Circuit',
            29: 'SNES Mario Circuit 3',
            30: 'DS Peach Gardens',
            31: 'GCN DK Mountain',
            32: 'N64 Bowser\'s Castle'
        }


class MockRandom(Random):

    def sample(self, sample_range, sample_size) -> list[int]:
        return [1, 2, 3, 4]


class TestRandomTracksSampler(TestCase):

    def setUp(self) -> None:
        self.sampler = RandomTracksSampler(MockTrackRepository(), MockRandom())

    def test_it_should_raise_exception_when_sample_size_is_lower_than_1(self):
        with self.assertRaises(SampleSizeShouldBeGreater):
            self.sampler.randomize(0)

    def test_it_should_raise_exception_when_sample_size_exceeds_total_track_size(self):
        with self.assertRaises(SampleSizeExceedsMaxTracksSize):
            self.sampler.randomize(33)

    def test_it_returns_a_formatted_list_of_tracks(self):
        actual_result = self.sampler.randomize(4)
        self.assertEqual(
            "Listing 4 randomized tracks:\n"
            "1: Luigi Circuit\n"
            "2: Moo Moo Meadows\n"
            "3: Mushroom Gorge\n"
            "4: Toad\'s Factory\n",
            actual_result
        )
