import re
from utils import read_file_by_line

result = 0
for line in read_file_by_line('y_2023/d_2/input.txt'):
    game, values = line.split(':')
    cube_max = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for value in values.split(';'):
        for cubes in value.split(','):
            for color, count in cube_max.items():
                if color in cubes:
                    cube_count = re.search(r'\d+', cubes)
                    if cube_count:
                        cube_max[color] = max(cube_max[color], int(cube_count.group()))
    line_result = 1
    for item in cube_max.values():
        line_result *= item
    result += line_result

print(result)
