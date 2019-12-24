# https://adventofcode.com/2019/day/3#part2

import re


def get_path(line) -> dict:
    x = 0
    y = 0
    long = 0
    result = {}
    for move, distance in re.findall(r"(\w)(\d*)", line):
        distance = int(distance)
        for i in range(distance):
            long += 1
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            key = f"{x}_{y}"
            if not result.get(key):
                result[key] = long
    return result


if __name__ == "__main__":
    with open('2019/3/input.txt', 'r') as input_file:
        line1, line2 = input_file

        path1 = get_path(line1)
        path2 = get_path(line2)

        distance = None
        for key in list(set(path1.keys()) & set(path2.keys())):
            point_distance = path1[key] + path2[key]
            if not distance or point_distance < distance:
                distance = point_distance
        print(distance)
