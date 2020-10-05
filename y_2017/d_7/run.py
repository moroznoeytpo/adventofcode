from collections import defaultdict
import re


matrix = defaultdict(list)
with open('y_2017/d_7/input.txt', 'r') as file:
    for line in file:
        if line:
            match = re.match(r"(\w+) \((\d+)\)( -> ([\w,\s]+))?", line.replace('\n', ''))
            if match:
                key = match.group(1)
                value = match.group(2)

                if match.group(3):
                    childs = match.group(4).split(', ')
                else:
                    childs = []
                matrix[key] = childs

top_key = None

for key, value in matrix.items():
    if not top_key or top_key in value:
        top_key = key
print(top_key)
