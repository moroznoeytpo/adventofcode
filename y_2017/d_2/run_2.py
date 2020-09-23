captcha = 0
with open('y_2017/d_2/input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split('\t')))
        index = 0
        for needle_index, needle_item in enumerate(row):
            for haystack_index, haystack_item in enumerate(row):
                if needle_index == haystack_index:
                    continue
                if needle_item % haystack_item == 0:
                    captcha += int(needle_item / haystack_item)

print(captcha)
