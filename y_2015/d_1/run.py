with open('2015/1/input.txt', 'r') as input_file:
	content = input_file.read()
	floor = 0
	for i in content:
		if i == '(':
			floor += 1
		elif i == ')':
			floor -= 1
print(floor)