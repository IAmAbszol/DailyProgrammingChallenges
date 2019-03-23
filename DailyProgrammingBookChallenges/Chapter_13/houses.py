def house(matrix):
	k = len(matrix[0])
	solution_row = [0 for i in len(k)]
	
	for r, row in enumerate(matrix):
		new_row = []
		for c, val in enumerate(row):
			new_row.append(min(solution_row[i] for i in range(k) if i != c) + val)
		solution_row = new_row
	print min(solution_row)
