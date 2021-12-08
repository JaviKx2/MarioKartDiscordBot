from src.TrackRepository import TrackRepository


class InMemoryTrackRepository(TrackRepository):

    numbered_tracks = {
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

    def find_all(self):
        return self.numbered_tracks

    def count_all(self):
        return len(self.numbered_tracks.keys())
