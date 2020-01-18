import json

def calculate(data) -> tuple:
	if isinstance(data, list):
		for item in data:
			yield  from calculate(item)
	elif isinstance(data, dict):
		if not 'red' in data.values():
			for key, value in data.items():
				yield from  calculate(value)
	elif isinstance(data, int):
		yield data

with open('2015/12/input.txt', 'r') as input_file:

	data = json.loads(input_file.read())
	total = 0
	for num in calculate(data):
		total += num
	print(total)
