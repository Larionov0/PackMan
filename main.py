class IMovable:
    def move(self, direction):
        raise Exception('метод не переназначен!')


class Solid:
    coords: int

    def __init__(self, coords):
        self.coords = coords


class Creature(Solid, IMovable):
    name: str
    coords: list

    def __init__(self, name, coords):
        super().__init__(coords)
        self.name = name

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

    def __init__(self, name, coords, coins=0):
        super().__init__(name, coords)
        self.coins = coins

    def __str__(self):
        return "+"


class Wall(Solid):
    def __str__(self):
        return "0"


class Field:
    matrix: list

    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, index):
        return self.matrix[index]

    @classmethod
    def __generate_coins_matrix(cls, n, m):
        matrix = []
        for i in range(n):
            row = [Coin()] * m
            matrix.append(row)
        return matrix

    @classmethod
    def create_matrix_with_objects(cls, hero_coords, walls_coords, n, m):
        matrix = cls.__generate_coins_matrix(n, m)
        field = cls(matrix)

        hero = Hero("Vasya", hero_coords)
        field.put_object_to_matrix(hero)

        for wall_coords in walls_coords:
            wall = Wall(wall_coords)
            field.put_object_to_matrix(wall)

        return field

    def put_object_to_matrix(self, obj):
        self[obj.coords[0]][obj.coords[1]] = obj

    def print(self):
        for row in self.matrix:
            for cell in row:
                print("%-3s" % str(cell), end=" ")
            print()


class Coin:
    def __str__(self):
        return "$"


field = Field.create_matrix_with_objects([1, 1], [[2, 2], [3, 2], [4, 2]], 10, 10)
field.print()
