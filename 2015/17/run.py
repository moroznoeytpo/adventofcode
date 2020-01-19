input_file = open('2015/17/input.txt', 'r')
containers = input_file.read().split('\n')

litres = 150
class Way:
    def __init__(self, litres: int, containers: list):
        self.litres = litres
        self.containers = list(map(int, containers))
        self.ways = []
        self.start = 0


    def collect(self):
        litres = self.litres
        way = []
        save = False
        print('=================')
        for i, item in enumerate(self.containers):
            if i < self.start:
                continue
            print(f'----{self.start}')
            print(f"litres = {litres}")
            print(f"[{i}] = {item}")
            if litres - item > 0:
                print(f'{litres}-{item}')
                litres -= item
                way.append(str(i))
            elif litres - item == 0:
                way_str = "-".join(way + [str(i)])
                if way_str not in self.ways:
                    print(f'save {way_str}')
                    litres -= item
                    save = True
                    self.ways.append(way_str)
        if not save:
            self.start += 1
        if self.start <= len(self.containers):
            self.collect()

obj = Way(litres, containers)
obj.collect()

print(obj.ways)
