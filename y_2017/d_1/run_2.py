with open('y_2017/d_1/input.txt', 'r') as file:
    content = file.read()

content = content.strip()
captcha = 0
index = 0
middle_index = int(len(content) / 2)

while(True):
    if index == middle_index:
        break
    if content[index] == content[index + middle_index]:
        captcha += int(content[index]) * 2
    index += 1
print(captcha)
