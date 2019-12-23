with open('2019/2/input.txt', 'r') as input_file:
    program = [int(item) for item in input_file.read().split(',')]

    def program_1202(program, position):
        if program[position] == 1:
            program[program[position + 3]] = program[program[position + 1]] + program[program[position + 2]]
            position += 4

        elif program[position] == 2:
            program[program[position + 3]] = program[program[position + 1]] * program[program[position + 2]]
            position += 4

        elif program[position] == 99:
            position = len(program)
        return position

    position = 0
    program[1] = 12
    program[2] = 2
    while position < len(program):
        position = program_1202(program, position)
    print(program[0])
