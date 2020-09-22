def program_1202(program) -> int:
    def get_modes(instrustion: int):
        instrustion_str = str(instrustion)
        result = []
        for index in range(len(instrustion_str)-3, -1, -1):
            result.append(int(instrustion_str[index]))
        if len(result) < 3:
            result += [0] * (3-len(result))
        return result

    def get_value(index: int, mode: int):
        if mode == 0:
            return program[program[index]]
        else:
            return program[index]

    i = 0
    buffer = None
    while(len(program) > i):
        print(program[i])
        if program[i] == 99:
            print('Exit', program)
            return program[0]

        elif program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            i += 4

        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            i += 4

        elif program[i] == 3:
            buffer = program[program[i+1]]
            i += 2

        elif program[i] == 4:
            program[program[i+1]] = buffer
            i += 2

        elif program[i] % 2 == 1:
            modes = get_modes(program[i])
            var_1 = get_value(i + 1, modes[0])
            var_2 = get_value(i + 2, modes[1])
            if modes[2] == 0:
                program[program[i + 3]] = var_1 + var_2
            else:
                program[i + 3] = var_1 + var_2
            i += 4

        elif program[i] % 2 == 0:
            modes = get_modes(program[i])
            var_1 = get_value(i + 1, modes[0])
            var_2 = get_value(i + 2, modes[1])
            if modes[2] == 0:
                program[program[i + 3]] = var_1 * var_2
            else:
                program[i + 3] = var_1 * var_2
            i += 4


if __name__ == "__main__":
    with open('y_2019/d_5/input.txt', 'r') as input_file:
        program = [int(item) for item in input_file.read().split(',')]
        program[1] = 12
        program[2] = 2

        print(program_1202(program))
