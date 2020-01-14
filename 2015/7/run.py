# https://adventofcode.com/2015/day/7


def find_variables(variables, results):
	for r_k, r_v in results.copy().items():
		for v_k, v_v in variables.copy().items():
			result = None
			if r_k not in v_v:
				continue
			if v_v[0] == 'NOT':
				result = 2**16 - r_v - 1
			elif v_v[0] == 'IS':
				result = r_v
			elif v_v[1] in ['AND', 'OR']:
				first = v_v.index(r_k)
				second = 0 if first else 2
				if isinstance(v_v[second], int):
					if v_v[1] == 'AND':
						result = r_v & int(v_v[second])
					else:
						result = r_v | int(v_v[second])
				else:
					variables[v_k][first] = r_v
			elif v_v[1] in ['LSHIFT', 'RSHIFT']:
				if v_v[1] == 'LSHIFT':
					result = r_v << int(v_v[2])
				else:
					result = r_v >> int(v_v[2])
			if not result is None:
				del (variables[v_k])
				results[v_k] = result
	return variables, results


with open('2015/7/input.txt', 'r') as input_file:
	variables = {}
	results = {}
	for line in input_file:
		result = line.split()
		key = result[-1]
		if result[0].isdigit():
			results[key] = int(result[0])
		elif result[0] == 'NOT':
			variables[key] = result[0:2]
		elif result[1] == '->':
			variables[key] = ['IS', result[0]]
		else:
			variables[key] = result[0:3]
	num = 0
	while variables:
		variables, results = find_variables(variables, results)
		# print('-----------------')
		# print(variables)
		# print(results)
		num +=1
	print(num)
	print(results.get('a'))
	print(results.get('m'))
	print(results.get('e'))

