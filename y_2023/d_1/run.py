from utils import read_file_by_line


result = 0
for line in read_file_by_line('y_2023/d_1/input.txt'):
    line_result = 0
    # Чтение с начала
    index = 0
    while index < len(line):
        point = line[index]
        if point.isdigit():
            line_result += int(point) * 10
            break
        index += 1
    # Чтение с конца
    index = len(line) - 1
    while index > -1:
        point = line[index]
        if point.isdigit():
            line_result += int(point)
            break
        index -= 1
    print(f'line={line_result}')
    result += line_result

print(f'total={result}')
