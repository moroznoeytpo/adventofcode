import re


class Molecules:
    def __init__(self, molecules: dict, starting: str):
        self.molecules = molecules
        self.starting = starting
        self.step = 0

    def remove(self):
        for key, value in self.molecules.items():
            for item in value:
                if item in self.starting:
                    self.step += self.starting.count(item)
                    self.starting = self.starting.replace(item, key)

    def find(self):
        for i in range(10):
            self.remove()
            print(self.starting)
            print(self.step)


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

obj = Molecules(molecules, starting)
obj.find()
