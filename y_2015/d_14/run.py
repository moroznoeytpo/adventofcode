from copy import copy
with open('2015/14/tmp.txt', 'r') as input_file:
    deers = []
    for line in input_file:
        split_line = line.split(' ')
        deers.append({
            'name': split_line[0],
            'speed': int(split_line[3]),
            'time': int(split_line[6]),
            'rest': int(split_line[-2]),
            'distance': 0,
            'flying': None,
            'resting': None
        })
    for i in range(1000):
        leaders = []
        lead_distance = None
        for deer in deers:
            if not deer['flying']and not deer['resting']:
                deer['flying'] = copy(deer['time'])
                deer['resting'] = copy(deer['rest'])
            if deer['flying']:
                deer['distance'] += deer['speed']
                deer['flying'] -= 1
            elif deer['resting']:
                deer['resting'] -= 1

    goodest_deer = None
    for deer in deers:
        if not goodest_deer or deer['distance'] > goodest_deer['distance']:
            goodest_deer = deer
    print('-----------------')
    print(goodest_deer)
