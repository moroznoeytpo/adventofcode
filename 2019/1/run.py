with open('2019/1/input.txt', 'r') as input_file:
    result = 0
    for item in input_file:
        result += int(item) // 3 - 2
print(result)
