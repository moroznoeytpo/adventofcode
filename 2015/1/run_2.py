with open('2015/1/input.txt', 'r') as input_file:
	content = input_file.read()
	floor = 1
	for i, move in enumerate(content):
		if move == '(':
			floor += 1
		elif move == ')':
			floor -= 1
		if floor == -1:
			print(i)
			break
