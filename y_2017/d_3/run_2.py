from collections import defaultdict
input_content = 347991

result_matrix = defaultdict(dict)

max_value = 0
result_matrix[0][0] = 1
x_index = 1
y_index = 0
direction = [1, 0]

while input_content > max_value:
    max_value = 0
    count = 0
    for x_range in range(-1, 2):
        for y_range in range(-1, 2):
            try:
                max_value += result_matrix[x_index + x_range][y_index + y_range]
                count += 1
            except KeyError:
                pass
    result_matrix[x_index][y_index] = max_value
    if count <= 2:
        if direction == [1, 0]:
            direction = [0, 1]
        elif direction == [0, 1]:
            direction = [-1, 0]
        elif direction == [-1, 0]:
            direction = [0, -1]
        elif direction == [0, -1]:
            direction = [1, 0]
        else:
            raise Exception
    x_index += direction[0]
    y_index += direction[1]

print(max_value)  # 349975
