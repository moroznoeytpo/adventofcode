from .run import program_1202


with open('2019/2/input.txt', 'r') as input_file:
    program = [int(item) for item in input_file.read().split(',')]

    for noun in range(99):
        for verb in range(99):
            program[1] = noun
            program[2] = verb

            phrase = list(program)
            if program_1202(phrase) == 19690720:
                print(100 * noun + verb)
