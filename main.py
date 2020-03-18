class IMovable:
    def move(self, direction, field):
        raise Exception('метод не переназначен!')


class Solid:
    coords: int

    def __init__(self, coords):
        self.coords = coords


class Creature(Solid, IMovable):
    __name: str
    coords: list

    def __init__(self, name, coords):
        super().__init__(coords)
        self.__name = name

    def move(self, direction, field):
        coords = self.coords.copy()

        if direction == "N":
            coords[0] -= 1
        elif direction == "E":
            coords[1] += 1
        elif direction == "S":
            coords[0] += 1
        elif direction == "W":
            coords[1] -= 1

        if field.check_possibility_of_moving_to_cell(coords):
            field.del_object_from_cell(self)
            self.coords = coords
            field.put_object_to_matrix(self)


class Hero(Creature):
    __coins: int
    queries: list

    def __init__(self, name, coords, queries, coins=0):
        super().__init__(name, coords)
        self.__coins = coins
        self.queries = queries

    def __str__(self):
        return "+"

    @property
    def coins(self):
        return self.__coins

    def add_coin(self):
        self.add_coins(1)

    def add_coins(self, coins):
        self.__coins += coins

    def move(self, direction, field):
        coords = self.coords.copy()

        if direction == "N":
            coords[0] -= 1
        elif direction == "E":
            coords[1] += 1
        elif direction == "S":
            coords[0] += 1
        elif direction == "W":
            coords[1] -= 1

        if field.check_possibility_of_moving_to_cell(coords):
            if isinstance(field.get_object_from_cell(coords), Coin):
                self.add_coin()
            field.del_object_from_cell(self)
            self.coords = coords
            field.put_object_to_matrix(self)

    def move_with_queries(self, field):
        for query in self.queries:
            self.move(query, field)


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
    def create_matrix_with_objects(cls, hero, walls, n, m):
        matrix = cls.__generate_coins_matrix(n, m)
        field = cls(matrix)

        field.put_object_to_matrix(hero)

        for wall in walls:
            field.put_object_to_matrix(wall)

        return field

    def put_object_to_matrix(self, obj):
        self[obj.coords[0]][obj.coords[1]] = obj

    def print(self):
        for row in self.matrix:
            for cell in row:
                print("%-4s" % str(cell), end=" ")
            print()

    def check_wall_on_cell(self, coords):
        return isinstance(self[coords[0]][coords[1]], Wall)

    def check_possibility_of_moving_to_cell(self, coords):
        if coords[0] < 0 or coords[0] >= len(self.matrix):
            return False
        if coords[1] < 0 or coords[1] >= len(self[0]):
            return False
        if self.check_wall_on_cell(coords):
            return False
        return True

    def del_object_from_cell(self, obj):
        self[obj.coords[0]][obj.coords[1]] = None

    def get_object_from_cell(self, coords):
        return self[coords[0]][coords[1]]


class Coin:
    def __str__(self):
        return "$"


class FileWrapper:
    def __init__(self, filepath):
        self.file = open(filepath)

    @classmethod
    def read_packman_info(cls, filepath='./packman_info.txt'):
        file = cls(filepath)
        n, m = file.read_two_numbers()
        hero_coords = file.read_two_numbers()
        queries = list(file.read_line())
        walls_coords = file.read_all_lines_with_numbers()
        file.close()
        return n, m, hero_coords, queries, walls_coords

    def read_two_numbers(self):
        return list(map(int, self.read_line().rstrip().split(' ')))

    def read_line(self):
        return self.file.readline().rstrip()

    def read_all_lines_with_numbers(self):
        lst = []
        for line in self.file:
            lst.append(list(map(int, line.rstrip().split(' '))))
        return lst

    def close(self):
        self.file.close()


def menu(field, hero):
    while True:
        field.print()
        print(f"Coins: {hero.coins}")
        choice = input()
        hero.move(choice, field)


def main():
    n, m, hero_coords, queries, walls_coords = FileWrapper.read_packman_info()
    walls = []
    for coords in walls_coords:
        walls.append(Wall(coords))

    hero = Hero("Bob", hero_coords, queries)

    field = Field.create_matrix_with_objects(hero, walls, n, m)

    hero.move_with_queries(field)
    print(f"{hero.coords[0]} {hero.coords[1]} {hero.coins}")


if __name__ == '__main__':
    main()
