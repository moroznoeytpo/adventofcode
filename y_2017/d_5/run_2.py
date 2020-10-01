values = []

with open('y_2017/d_5/input.txt', 'r') as file:
    for line in file:
        if line:
            values.append(int(line))

position = 0
step = 0
while(True):
    try:
        current_value = values[position]
        if current_value < 3:
            values[position] += 1
        else:
            values[position] -= 1

        position += current_value
        step += 1
    except IndexError:
        print(step)
        break
