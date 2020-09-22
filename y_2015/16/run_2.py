my_aunt = {
    'children': 3,
    'cats': ('>', 7),
    'samoyeds': 2,
    'pomeranians': ('<', 3),
    'akitas': 0,
    'vizslas': 0,
    'goldfish': ('<', 5),
    'trees': ('>', 3),
    'cars': 2,
    'perfumes': 1
}
import re

def is_my_aunt(aunt, my_aunt) -> bool:
    for key, value in aunt.items():
        if key not in my_aunt:
            return False
        if isinstance(my_aunt[key], tuple):
            if (my_aunt[key][0] == '>' and my_aunt[key][1] >= value) \
                    or (my_aunt[key][0] == '<' and my_aunt[key][1] <= value):
                return False
        elif my_aunt[key] != value:
            return False
    return True

with open('2015/16/input.txt', 'r') as input_file:
    aunts = []
    for line in input_file:
        aunt = {}
        rate = 0
        match = re.search(r"^Sue (\d+)", line)
        for item in re.findall(r"(\w+): (\d+)", line, flags=re.DOTALL):
            aunt[item[0]] = int(item[1])
        if is_my_aunt(aunt, my_aunt):
            print(match[1])
            print(aunt)

