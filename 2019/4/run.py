# https://adventofcode.com/2019/day/4

from contextlib import suppress

count = 0

for password in range(272091, 815432):
    password = str(password)

    increase = True
    adjacent = False
    for i in range(len(password)):
        with suppress(IndexError):
            if password[i] > password[i+1]:
                increase = False
                continue
            if password[i] == password[i + 1]:
                adjacent = True
    if increase and adjacent:
        count += 1

print(count)
