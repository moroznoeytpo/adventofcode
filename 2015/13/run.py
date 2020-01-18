def get_way(matrix: dict, start: str, way: list, total_distance: int) -> tuple:
    new_way = way + [start]
    if len(new_way) == len(matrix):
        end = way[0]
        distance = matrix[start][end]
        yield from get_way(matrix, end, new_way, total_distance + distance)
    elif len(new_way) > len(matrix):
        yield new_way, total_distance
    for end, distance in matrix[start].items():
        if end in way:
            continue
        else:
            yield from get_way(matrix, end, new_way, total_distance + distance)


with open('2015/13/input.txt', 'r') as input_file:
    matrix = {}
    for line in input_file:
        split_line = line[0:-2].split(' ')
        name1 = split_line[0]
        name2 = split_line[10]
        if split_line[2] == 'gain':
            weight = int(split_line[3])
        else:
            weight = -int(split_line[3])

        if not matrix.get(name1):
            matrix[name1] = {}
        if matrix[name1].get(name2):
            matrix[name1][name2] += weight
        else:
            matrix[name1][name2] = weight

        if not matrix.get(name2):
            matrix[name2] = {}
        if matrix[name2].get(name1):
            matrix[name2][name1] += weight
        else:
            matrix[name2][name1] = weight

    min_way = None
    max_way = None
    for start in matrix.keys():
        for item in get_way(matrix, start, [], 0):
            if not min_way or item[1] < min_way[1]:
                min_way = item
            if not max_way or item[1] > max_way[1]:
                max_way = item
    print(min_way)
    print(max_way)
