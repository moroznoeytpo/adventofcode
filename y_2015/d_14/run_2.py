from copy import copy
with open('2015/14/input.txt', 'r') as input_file:
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
            'resting': None,
            'lead_point': 0
        })
    for i in range(2503):
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

            if not lead_distance:
                lead_distance = deer['distance']
            if deer['distance'] > lead_distance:
                lead_distance = deer['distance']
                leaders = [deer]
            elif deer['distance'] == lead_distance:
                leaders.append(deer)
        for leader in leaders:
            leader['lead_point'] += 1

    goodest_deer = None
    for deer in deers:
        if not goodest_deer or deer['lead_point'] > goodest_deer['lead_point']:
            goodest_deer = deer
    print(goodest_deer)
