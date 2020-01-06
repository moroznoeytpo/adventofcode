# https://adventofcode.com/2015/day/5

with open('2015/5/input.txt', 'r') as input_file:
	only = ['a', 'e', 'i', 'o', 'u']
	not_containt = ["ab", "cd", "pq", "xy"]
	total = 0
	for text in input_file:
		need = 0
		double = 0
		incr = 0
		l = len(text)
		for i in range(len(text)):
			if text[i] in only:
				need += 1
			if i == l - 1:
				break
			s = ord(text[i])
			s_n = ord(text[i + 1])
			if s == s_n:
				double += 1
		for i in not_containt:
			if i in text:
				incr += 1
		if need > 2 and double and not incr:
			total += 1
	print(total)