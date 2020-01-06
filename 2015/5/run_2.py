# https://adventofcode.com/2015/day/5#part2

with open('2015/5/input.txt', 'r') as input_file:
	total = 0
	for text in input_file:
		mirror = 0
		double = 0

		l = len(text)
		for i in range(l):
			if i == l - 2:
				break
			if i <= l - 4 and text[i] == text[i + 2]:
				mirror += 1
			let = text[i:i + 2]
			for j in range(i+2, l):
				if j == l - 2:
					break
				let2 = text[j:j + 2]
				if let == let2:
					double += 1
		if mirror and double:
			total += 1
	print(total)