class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lenght = 0
        self.objs = []

    def __len__(self):
        return int(self.lenght)

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.lenght += ((tr.to_x - self.start_x) ** 2 + (tr.to_y - self.start_y) ** 2) ** 0.5
            self.start_x = tr.to_x
            self.start_y = tr.to_y
            self.objs.append(tr)

    def get_tracks(self):
        return tuple(self.objs)

    def __eq__(self, other):
        if isinstance(other, Track):
            return self.lenght == other.lenght

    def __gt__(self, other):
        if isinstance(other, Track):
            return self.lenght > other.lenght


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
