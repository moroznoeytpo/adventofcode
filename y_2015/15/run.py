import re

with open('2015/15/tmp.txt', 'r') as input_file:
    ingredients = {}
    for line in input_file:
        match = re.search(r"^(\w*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)", line, flags=re.DOTALL)
        ingredients[match[1]] = {
            'property': {
                'capacity': int(match[2]),
                'durability': int(match[3]),
                'flavor': int(match[4]),
                'texture': int(match[5]),
                # 'calories': int(match[6]),
        }}
    persent = 44
    ingredients['Butterscotch']['percent'] = persent
    ingredients['Cinnamon']['percent'] = 100 - persent

    total = {}
    for ingredient in ingredients.values():
        percent = ingredient['percent']
        for key, value in ingredient['property'].items():
            key_persent = percent * value
            if not total.get(key):
                total[key] = key_persent
            else:
                total[key] += key_persent
    multiple_score = 1
    for value in total.values():
        if value < 0:
            value = 0
        multiple_score *= value
    print(total)
    print(multiple_score)
