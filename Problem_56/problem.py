'''

4 verticies

	1 2 3 4
1 	0 1	1 0
2	1 0 0 0
3   1 0 0 1
4	0 0 1 0

Verticies from 1 to 4
colors = [Red, Green, Blue], k = 2
Let 1 be 1 --> colors[1] = Red
Let 2 be 1 --> Error, adjacent element is 1
Let 2 be 2 --> colors[2] = Green
Let 3 be 1 --> Error, adjacent element is 1
Let 3 be 2 --> Colors[2] = Green
Let 4 be 1 --> Colors[1] = Red
Successfully placed all colors, return True

k = 1
Let 1 be 1 --> colors[1] = Red
Let 2 be 1 --> Error, adjacent element is 1
False, exceeded range and still have more elements, return False

'''

def solve(matrix, k):
	colors = []

	return backtrack(matrix, colors, 0, k)


def backtrack(matrix, colors, node, k):
	if node >= len(matrix):
		return True

	for sub_k in range(k):
		colors.append(sub_k)
		if is_valid(matrix, colors):
			if backtrack(matrix, colors, node + 1, k):
				return True
		colors.pop()
	return False

def is_valid(matrix, colors):
	for node in range(len(matrix)):
		if node > len(colors) - 1:
			return True
		indicies = all_adjacent_index(matrix, node)
		for idx in indicies:
			if idx > len(colors) - 1:
				continue
			if colors[node] == colors[idx]:
				return False
	return True

def all_adjacent_index(matrix, node):
	return [idx for idx, val in enumerate(matrix[node]) if val == 1]


#matrix = [[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]]
matrix = [[0,1,0,1],[1,0,1,1],[0,1,0,0],[1,1,0,0]]
k = 3

print(solve(matrix, k))