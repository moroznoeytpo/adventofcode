import re


class Molecules:
    def __init__(self, molecules: dict, starting: str):
        self.e = molecules.pop('e')
        self.molecules = molecules
        self.starting = starting
        self.result = set(self.e)
        self.step = 1

    def run(self):
        result = set()
        for line in self.result:
            length = len(line)
            for key, value in self.molecules.items():
                shift = len(key)
                if key not in line:
                    result.add(line)
                    continue
                i = 0
                while True:
                    i = line.find(key, i)
                    if i < 0:
                        break
                    for item in value:
                        result.add(line[0:i] + item + line[i + shift:length])
                    i += 1
        self.result = result

    def find(self):
        while True:
            self.run()
            self.step += 1
            print(self.step)
            if self.starting in self.result:
                break


input_file = open('2015/19/input.txt', 'r')
molecules = {}
starting = None
for line in input_file:
    match = re.search(r'(\w+) => (\w+)', line)
    if match:
        if not molecules.get(match[1]):
            molecules[match[1]] = []
        molecules[match[1]].append(match[2])
    elif re.search(r"\w+", line):
        starting = line

molecules['e'] = ['H', 'O']

obj = Molecules(molecules, starting)
obj.find()
print(obj.step)
