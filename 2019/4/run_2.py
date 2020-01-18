from contextlib import suppress

count = 0

for password in range(272091, 815432):
    password = str(password)

    increase = True
    adjacent = {}
    for i in range(len(password) - 1):
        if password[i] > password[i+1]:
            increase = False
            continue
        if password[i] == password[i + 1]:
            if not adjacent.get(password[i]):
                adjacent[password[i]] = 2
            else:
                adjacent[password[i]] += 1
    result = [k for k, v in adjacent.items() if v == 2]
    if increase and result:
        count += 1

print(count)
