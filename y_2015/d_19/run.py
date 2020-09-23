import re


class Molecules:
    def __init__(self, molecules: dict, starting: str):
        self.molecules = molecules
        self.starting = starting
        self.length = len(self.starting)
        self.result = set()

    def run(self):
        for i in range(self.length):
            key = None
            shift = 1
            try:
                if self.starting[i] in self.molecules:
                    key = self.starting[i]
                elif self.starting[i] + self.starting[i+1] in self.molecules:
                    key = self.starting[i] + self.starting[i+1]
                    shift = 2
                if key:
                    for item in self.molecules[key]:
                        self.result.add(self.starting[0:i] + item + self.starting[i+shift:self.length])
            except IndexError:
                pass


input_file = open('2015/19/input.txt', 'r')

new_molecules = set()
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
obj.run()
print(obj.molecules)
print(obj.starting)
print(len(obj.result))
