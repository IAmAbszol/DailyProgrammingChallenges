def add_key(dictionary, a, b):
	if b in dictionary.keys():
		dictionary[b].append(a)
		# Remove random duplicates
		dictionary[b] = list(set(dictionary[b]))
		return
	dictionary[b] = [a]

def has_cycle(dictionary, element, recursion_list=None):
	if not bool(dictionary):
		return False
	if element is None:
		element = list(dictionary.keys())[0]
	if recursion_list is None:
		recursion_list = []
	if element in recursion_list:
		return True
	recursion_list.append(element)
	if element not in dictionary.keys():
		return False

	# Update element
	ls = dictionary[element]
	# Is empty, were at the end
	if not ls:
		return False
	# Remove value from list
	val = ls[0]
	dictionary[element].remove(val)
	element = val
	return has_cycle(dictionary, element, recursion_list)

def problem(instruction):
	'''
		North case
		dict[b] = [a]
		dict[c] = [b]
		dict[a] = [c]

		recurse through, use list to keep recursion stack. if any appear, cycle!
	
	'''

	n_dict = {}
	s_dict = {}
	e_dict = {}
	w_dict = {}

	for instruct in instruction:
		a, i, b = instruct
		for c in i:
			if c == 'N':
				add_key(n_dict, a, b)
			elif c == 'S':
				add_key(s_dict, a, b)
			elif c == 'E':
				add_key(e_dict, a, b)
			elif c == 'W':
				add_key(w_dict, a, b)

	if any([has_cycle(n_dict, None), has_cycle(s_dict, None), has_cycle(e_dict, None), has_cycle(w_dict, None)]):
		return False
	return True
					
instructions = [[['A', 'N', 'B'],['B', 'NE', 'C'],['C','N','A']],
				[['A', 'NW', 'B'],['A','N','B']]]


print(problem(instructions[0]))
print(problem(instructions[1]))
