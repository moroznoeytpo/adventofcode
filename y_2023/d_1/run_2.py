from utils import read_file_by_line


nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
line_count = 0
result = 0
for line in read_file_by_line('y_2023/d_1/input.txt'):
    line_result = 0
    # Чтение с начала
    index = 0
    flag = True
    while index < len(line) and flag:
        point = line[index]
        if point.isdigit():
            line_result += int(point) * 10
            flag = False
        else:
            for num, dig in nums.items():
                if line[index:index+len(num)] == num:
                    line_result += dig * 10
                    flag = False
                    break
        index += 1
    # Чтение с конца
    index = len(line) - 1
    flag = True
    while index > -1 and flag:
        point = line[index]
        if point.isdigit():
            line_result += int(point)
            flag = False
        else:
            for num, dig in nums.items():
                if line[index-len(num)+1:index+1] == num:
                    line_result += dig
                    flag = False
                    break
        index -= 1
    line_count += 1
    print(f'line {line_count}={line_result}')
    result += line_result

print(f'total={result}')
