from collections import defaultdict
import re


matrix = defaultdict(dict)
with open('y_2017/d_7/input.txt', 'r') as file:
    for line in file:
        if line:
            match = re.match(r"(\w+) \((\d+)\)( -> ([\w,\s]+))?", line.replace('\n', ''))
            if match:
                key = match.group(1)
                value = int(match.group(2))

                if match.group(3):
                    childs = match.group(4).split(', ')
                else:
                    childs = []
                matrix[key] = {'weight': value, 'childs': childs, 'tree_weight': 0}


def tree_weight(name: str):
    item = matrix[name]
    weight = 0

    childs_weights = defaultdict(list)
    for child_name in item['childs']:
        child_tree_weight = tree_weight(child_name)
        matrix[child_name]['tree_weight'] = child_tree_weight

        childs_weights[child_tree_weight].append(child_name)

        weight += child_tree_weight

    if childs_weights:
        if max(childs_weights) != min(childs_weights):
            delta = max(childs_weights) - min(childs_weights)
            for child_name in childs_weights[max(childs_weights)]:
                max_child = matrix[child_name]
                print(child_name, max_child, delta, max_child['weight'] - delta)

    weight += item['weight']

    matrix[name]['tree_weight'] = weight
    return weight


for key in matrix.keys():
    tree_weight(key)
