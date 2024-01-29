import re
from utils import read_file_by_line

possible = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
result = 0
for line in read_file_by_line('y_2023/d_2/input.txt'):
    is_possible = True
    game, values = line.split(':')
    try:
        for value in values.split(';'):
            for cubes in value.split(','):
                for color, count in possible.items():
                    if color in cubes:
                        cube_count = re.search(r'\d+', cubes)
                        if not cube_count or int(cube_count.group()) > count:
                            raise ValueError
        game_number = re.search(r'\d+', game)
        if game_number:
            result += int(game_number.group())
    except ValueError:
        pass
print(result)
