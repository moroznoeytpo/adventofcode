count = 0

with open('y_2017/d_4/input.txt', 'r') as file:
    for line in file:
        if line:
            words = line[:-1].split(' ')
            if words and len(words) == len(set(words)):
                count += 1

print(count)
