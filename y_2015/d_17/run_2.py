class Way:
    def __init__(self, litres: int, containers: list):
        self.litres = litres
        self.containers = containers
        self.ways = {}
        self.new_ways = {}
        self.result_ways = {}

    def collect(self):
        for i, item in enumerate(containers):
            self.new_ways = {}
            if self.ways:
                for path, length in self.ways.items():
                    self.append_new_way(path, length, i, item)
                    self.append_new_way(path, length, i, 'x')
            else:
                self.append_new_way("", 0, i, item)
                self.append_new_way("", 0, i, 'x')
            self.ways.update(self.new_ways)

    def append_new_way(self, way_path: str, way_length: int, item_i: int, item_length: str) -> None:
        if item_length.isdigit():
            item_length = way_length + int(item_length)
            if item_length > self.litres:
                return None
        else:
            item_length = way_length
            item_i = 'x'
        key = f"{way_path}-{item_i}"
        if item_length == self.litres:
            real_path = key.replace('-x', '')
            if real_path not in self.result_ways:
                self.result_ways[real_path] = item_length
        else:
            self.new_ways[key] = item_length


input_file = open('2015/17/input.txt', 'r')
containers = input_file.read().split('\n')

litres = 150
obj = Way(litres, containers)
obj.collect()

min_length = None
total_count = 0
for path, length in obj.result_ways.items():
    count = path.count('-')
    if not min_length or min_length > count:
        total_count = 1
        min_length = count
    elif min_length == count:
        total_count += 1
print(min_length)
print(total_count)
