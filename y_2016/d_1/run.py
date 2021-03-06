class StreetGrid:
    def __init__(self, filename: str = 'tmp.txt'):
        self.filename = filename
        self.position = [0, 0]
        # 1 - 0
        # 2 - 90
        # 3 - 180
        # 4 - 270
        self.direction = 1
        self.index = 0
        self.data = None
        self.point = 0

    def get_directions(self) -> tuple:
        with open(f'2016/1/{self.filename}') as file:
            for item in file.read().split():
                yield item

    def set_point(self) -> None:
        # Ось движения
        self.point = self.index % 2
        self.index += 1

    def set_data(self, item) -> None:
        self.data = item[0], int(''.join([s for s in item if s.isdigit()]))

    def set_position(self):
        # Направление движения
        if (self.data[0] == 'R' and self.direction in [1, 4]) or (self.data[0] == 'L' and self.direction in [2, 3]):
            self.position[self.point] += self.data[1]
        elif (self.data[0] == 'R' and self.direction in [2, 3]) or (self.data[0] == 'L' and self.direction in [1, 4]):
            self.position[self.point] -= self.data[1]
        else:
            raise Exception('not perform type')

    def set_direction(self):
        if self.data[0] == 'R':
            self.direction += 1
            if self.direction > 4:
                self.direction = 1
        else:
            self.direction -= 1
            if self.direction < 1:
                self.direction = 4

    def calculate_direction(self, item):
        self.set_data(item)
        self.set_point()
        self.set_position()
        self.set_direction()

    def calculate(self):
        for item in self.get_directions():
            self.calculate_direction(item)

    def get_distance(self):
        return abs(self.position[0]) + abs(self.position[1])


if __name__ == '__main__':
    obj = StreetGrid('input.txt')
    obj.calculate()
    print(obj.get_distance())
