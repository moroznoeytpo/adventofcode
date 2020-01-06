# https://adventofcode.com/2015/day/3

with open('2015/3/input.txt', 'r') as input_file:
	x, y = 0, 0
	houses = [(x, y)]
	for move in input_file.read():
		if move == '>':
			x += 1
		elif move == '<':
			x -= 1
		elif move == '^':
			y += 1
		elif move == 'v':
			y -= 1
		if (x,y) not in houses:
			houses.append((x,y))
	print(len(houses))
