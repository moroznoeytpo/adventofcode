import re

with open('2015/6/input.txt', 'r') as input_file:

	l = 1000
	grid = [[0 for j in range(l)] for i in range(l)]
	total = 0
	for rule in input_file:
		match = re.search(r"([\w\s]*) (\d*),(\d*) through (\d*),(\d*)", rule)
		for i in range(int(match[2]), int(match[4]) + 1):
			for j in range(int(match[3]), int(match[5]) + 1):
				if match[1] == 'turn on':
					grid[i][j] += 1
					total += 1
				elif match[1] == 'turn off':
					if grid[i][j]:
						grid[i][j] -= 1
						total -= 1
				else:
					grid[i][j] += 2
					total += 2
	print(total)