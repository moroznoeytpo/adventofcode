# https://adventofcode.com/2015/day/2

with open('2015/2/input.txt', 'r') as input_file:
	square = 0
	for cube in input_file:
		l, w, h = cube.split('x')
		l, w, h = int(l), int(w), int(h)
		small = l*w*h / max(l, w, h)
		square += 2*l*w + 2*w*h + 2*h*l + small
	print(square)