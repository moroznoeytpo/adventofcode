from copy import deepcopy


class Grid:
    def __init__(self, grid: list):
        self.grid = grid

    def turn(self):
        new_drid = deepcopy(self.grid)
        for i, line in enumerate(self.grid):
            for j, point in enumerate(line):
                neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        try:
                            if x == 0 and y == 0:
                                continue
                            if i+x < 0 or j+y < 0:
                                continue
                            if self.grid[i+x][j+y] == '#':
                                neighbors += 1
                        except IndexError:
                            pass
                if point == '#' and neighbors not in [2, 3]:
                    new_drid[i][j] = '.'
                elif point == '.' and neighbors == 3:
                    new_drid[i][j] = '#'
        self.grid = new_drid


open = open('2015/18/input.txt', 'r')
grid = []
for line in open:
    ligths = []
    for j in range(0, len(line)-1):
        ligths.append(line[j])
    grid.append(ligths)

obj = Grid(grid)
for _ in range(100):
    obj.turn()

count = 0
for line in obj.grid:
    for point in line:
        if point == '#':
            count += 1
print(count)

