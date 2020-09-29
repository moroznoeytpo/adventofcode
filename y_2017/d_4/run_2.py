count = 0

with open('y_2017/d_4/input.txt', 'r') as file:
    for line in file:
        if line:
            words = []
            is_valid = True
            for item in line[:-1].split(' '):
                key = sorted(item)
                if key in words:
                    is_valid = False
                    break
                words.append(key)
            if is_valid:
                count += 1
print(count)
