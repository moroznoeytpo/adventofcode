infinitive_loop = []
with open('y_2017/d_6/input.txt', 'r') as file:
    content = [int(item) for item in file.read().split('\t') if item]

step = 0
current_index = 0
find_index = 0

try:
    while(True):
        insert_content = tuple(content)

        if insert_content in infinitive_loop:
            print(step)
            break

        infinitive_loop.append(insert_content)

        step += 1

        current_value = max(content)
        current_index = content.index(current_value)

        content[current_index] = 0
        while current_value > 0:
            if current_index == len(content) - 1:
                current_index = 0
            else:
                current_index += 1
            content[current_index] += 1
            current_value -= 1
except Exception:
    print(step, current_index - find_index)
