with open('2015/3/input.txt', 'r') as input_file:
	santa_x, santa_y = 0, 0
	robo_x, robo_y = 0, 0
	houses = [(santa_x, santa_y)]
	command = input_file.read()
	for i in range(0, len(command), 2):
		santa_move = command[i]
		if santa_move == '>':
			santa_x += 1
		elif santa_move == '<':
			santa_x -= 1
		elif santa_move == '^':
			santa_y += 1
		elif santa_move == 'v':
			santa_y -= 1
		if (santa_x, santa_y) not in houses:
			houses.append((santa_x, santa_y))

		robo_move = command[i+1]
		if robo_move == '>':
			robo_x += 1
		elif robo_move == '<':
			robo_x -= 1
		elif robo_move == '^':
			robo_y += 1
		elif robo_move == 'v':
			robo_y -= 1
		if (robo_x, robo_y) not in houses:
			houses.append((robo_x, robo_y))

	print(len(houses))
