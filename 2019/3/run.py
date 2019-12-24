import re

def get_path(line) -> list:
    x = 0
    y = 0
    result = []
    for move, distance in re.findall(r"(\w)(\d*)", line):
        distance = int(distance)
        for i in range(distance):
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            result.append((y, x))
    return result


with open('2019/3/input.txt', 'r') as input_file:
    line1, line2 = input_file

    path1 = get_path(line1)
    path2 = get_path(line2)

    distance = None
    for x, y in list(set(path1) & set(path2)):
        point_distance = abs(x) + abs(y)
        if not distance or point_distance < distance:
            distance = point_distance
    print(distance)
