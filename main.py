class IMovable:
    def move(self, direction):
        raise Exception('метод не переназначен!')


class Creature(IMovable):
    name: str
    coords: list

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def move(self, direction):
        if direction == "N":
            pass
        elif direction == "E":
            pass
        elif direction == "S":
            pass
        elif direction == "W":
            pass


class Hero(Creature):
    coins: int

    def __init__(self, name, coords, coins):
        super().__init__(name, coords)
        self.coins = coins
