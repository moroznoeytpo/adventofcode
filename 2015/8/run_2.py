with open('2015/8/input.txt', 'r') as input_file:
    diff_count = 0
    for line in input_file:
        i = 0
        l = len(line) - 1
        while i <= l:
            sym = line[i]
            if sym in ['\\', '"', '\'']:
                diff_count += 1
            i += 1
        diff_count += 2
    print(diff_count)
