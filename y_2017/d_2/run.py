captcha = 0
with open('y_2017/d_2/input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split('\t')))
        if row:
            captcha += max(row) - min(row)
print(captcha)
