class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.vel = v
        self.incr = i

    def increase(self):
        self.vel += self.incr

    def __repr__(self) -> str:
        return str(self.vel)


