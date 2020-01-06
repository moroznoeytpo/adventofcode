# https://adventofcode.com/2015/day/2

with open('2015/2/input.txt', 'r') as input_file:
	square = 0
	for cube in input_file:
		l, w, h = cube.split('x')
		l, w, h = int(l), int(w), int(h)
		feet = 2*l + 2*w + 2*h - 2*max(l, w, h)
		square += l*w*h + feet
	print(square)