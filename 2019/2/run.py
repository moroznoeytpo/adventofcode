# https://adventofcode.com/2019/day/2


def program_1202(program) -> int:
    for i in range(0, len(program), 4):
        if program[i] == 99:
            return program[0]
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]

        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]


if __name__ == "__main__":
    with open('2019/2/input.txt', 'r') as input_file:
        program = [int(item) for item in input_file.read().split(',')]
        program[1] = 12
        program[2] = 2

        print(program_1202(program))
