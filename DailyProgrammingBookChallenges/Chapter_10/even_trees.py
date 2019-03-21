'''
	This approach requires maximum edges to remove to get these trees to become even.

	This type of approach seems to be greedy as hinted by the keyword maximum.


	Sum up each vertex and count the number of descendants per node
'''

from collections import defaultdict

def traverse(graph, curr, result):
	descendants = 0

	for child in graph[curr]:
		num_nodes, result = traverse(graph, child, result)
		
		result[child] += num_nodes - 1
		descendants += num_nodes

	return descendants + 1, result

def maximum_edges(graph):
	start = list(graph)[0]
	vertices = defaultdict(int)

	_, descendants = traverse(graph, start, vertices)
	print(descendants)
	return len([val for val in descendants.values() if val % 2 == 1])

graph = {
	1: [2,3],
	2: [],
	3: [4,5],
	4: [6,7,8],
	5: [],
	6: [],
	7: [],
	8: []
}
print(maximum_edges(graph))

graph= { 
	1: [2,3],
	2: [],
	3: [4,5],
	4: [],
	5: []
}
print(maximum_edges(graph))
