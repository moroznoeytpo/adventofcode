from copy import deepcopy


class Grid:
    def __init__(self, grid: list):
        self.grid = grid

    def turn(self):
        for i, line in enumerate(deepcopy(self.grid)):
            for j, point in enumerate(line):
                neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        try:
                            if x == 0 and y == 0:
                                continue
                            if i+x < 0 or j+y < 0:
                                continue
                            if i == 0 and j == 2 and x == -1 and y == 0:
                                print(self.grid[i+x][j+y])

                            if self.grid[i+x][j+y] == '#':
                                # if i == 0 and j == 2:
                                #     print(self.grid[i+x][j+z])
                                neighbors += 1
                        except IndexError:
                            pass
                if point == '#' and neighbors not in [2, 3]:
                    self.grid[i][j] = '.'
                elif point == '.' and neighbors == 3:
                    self.grid[i][j] = '#'


open = open('2015/18/tmp.txt', 'r')
grid = []
for line in open:
    ligths = []
    for j in range(0, len(line)-1):
        ligths.append(line[j])
    grid.append(ligths)

obj = Grid(grid)
for line in obj.grid:
    print("".join(line))
print('----------------')
obj.turn()

for line in obj.grid:
    print("".join(line))

