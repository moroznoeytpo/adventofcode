# https://adventofcode.com/2015/day/8


with open('2015/8/input.txt', 'r') as input_file:
    diff_count = 0
    for line in input_file:
        i = 0
        l = len(line) - 1
        while i <= l:
            sym = line[i]
            if i == 0 or i == l:
                i += 1
                diff_count += 1
            elif sym == '\\':
                hexadecimal = set("0123456789abcdef")
                if line[i+1] in ['\\', '"', '\'']:
                    diff_count += 1
                    i += 2
                elif line[i+1] == 'x' and line[i+2] in hexadecimal and line[i+3] in hexadecimal:
                    diff_count += 3
                    i += 4
                else:
                    i += 1
            else:
                i += 1
    print(diff_count)
