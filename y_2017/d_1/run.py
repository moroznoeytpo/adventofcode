with open('y_2017/d_1/input.txt', 'r') as file:
    content = file.read()

content = content.strip()
captcha = 0
index = -1

while(True):
    if index == len(content) - 1:
        break
    if content[index] == content[index + 1]:
        captcha += int(content[index])
    index += 1

print(captcha)
