from copy import deepcopy


class Grid:
    def __init__(self, grid: list):
        self.grid = grid
        self.step = 0
        self.length = len(self.grid)
        self.base_point = [0, self.length - 1]
        self.count_on = 0

    def set_default(self):
        current_point, next_point = self.get_points()
        for x in self.base_point:
            for y in self.base_point:
                self.grid[x][y][current_point] = '#'
                self.grid[x][y][next_point] = '#'

    def get_points(self):
        return self.step % 2, 1 - self.step % 2

    def get_count(self):
        result = 0
        current_point, next_point = self.get_points()
        for line in self.grid:
            for point in line:
                if point[current_point] == '#':
                    result += 1
        return result

    def next_step(self):
        self.step += 1

    def turn(self):
        current_point, next_point = self.get_points()
        self.count_on = 0

        for i, line in enumerate(self.grid):
            for j, points in enumerate(line):
                neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        try:
                            if not x and not y:
                                continue
                            if i+x < 0 or j+y < 0:
                                continue
                            # if i == 4 and j == 0:
                            #     print(f"[{i+x}:{j+y}]", f"[{x}:{y}]", f">>{self.grid[i+x][j+y][current_point]}<<")
                            if self.grid[i+x][j+y][current_point] == '#':
                                neighbors += 1
                        except IndexError:
                            pass
                # if i == 4 and j == 0:
                #     print(i, j, current_point, neighbors, points)
                if points[current_point] == '#':
                    if neighbors in [2, 3]:
                        points[next_point] = '#'
                    else:
                        points[next_point] = '.'
                elif points[current_point] == '.':
                    if neighbors == 3:
                        points[next_point] = '#'
                    else:
                        points[next_point] = '.'
                else:
                    raise NotImplemented

    def print_grid(self):
        current_point, _ = self.get_points()
        print('===PRINT===')
        for line in self.grid:
            result = ""
            for point in line:
                result += point[current_point]
            print(result)


open = open('2015/18/input.txt', 'r')
grid = []
for line in open:
    ligths = []
    for j in range(0, len(line)-1):
        ligths.append([line[j], '.'])
    grid.append(ligths)

obj = Grid(grid)
for _ in range(100):
    obj.set_default()
    # obj.print_grid()
    obj.turn()
    obj.next_step()
else:
    obj.set_default()
    # obj.print_grid()
print(obj.get_count())

