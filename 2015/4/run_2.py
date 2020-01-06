# https://adventofcode.com/2015/day/4#part2

from hashlib import md5

line = 'iwrupvqb'
i = 0

while True:
	s = f"{line}{i}".encode()
	hash = md5(s).hexdigest()

	if hash.startswith('000000'):
		print(i)
		break
	i += 1