def get_way(matrix: dict, start: str, way: list, total_distance: int) -> tuple:
    new_way = way + [start]
    if len(new_way) == len(matrix):
        yield new_way, total_distance
    for end, distance in matrix[start].items():
        if end in way:
            continue
        else:
            yield from get_way(matrix, end, new_way, total_distance + distance)


def print_matrix(matrix: dict):
    keys = matrix.keys()
    result = "\t"
    for key in keys:
        result += f"{key[0:5]}\t"
    print('-' * 8 * (len(keys)+1))
    print(result)
    for start, target in matrix.items():
        result = f"{start[0:5]}\t"
        for end in matrix.keys():
            if target.get(end):
                result += f"{target[end]}\t"
            else:
                result += f"x\t"
        print(result)
    print('-' * 8 * (len(keys)+1))


with open('2015/9/input.txt', 'r') as input_file:
    matrix = {}
    for line in input_file:
        start, _, end, _, distance = line.split(' ')
        distance = int(distance)
        if not matrix.get(start):
            matrix[start] = {}
        matrix[start][end] = distance

        if not matrix.get(end):
            matrix[end] = {}
        matrix[end][start] = distance
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
    print_matrix(matrix)
