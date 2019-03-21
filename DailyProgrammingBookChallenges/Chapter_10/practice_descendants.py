from collections import defaultdict

'''
	I've never actually created a defaultdict to manage descendants, wanted to try.
	I could actually convert this into the even tree problem if we exclude the returned root.
'''

def descendants(graph, node, graph_dict):
	if not graph[node]:
		return 1
	sum_nodes = 0
	for child in graph[node]:
		sum_nodes += descendants(graph, child, graph_dict)
	graph_dict[node] += sum_nodes
	return sum_nodes + 1

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

graph_dict = defaultdict(int)
print(descendants(graph, list(graph)[0], graph_dict))
print(graph_dict)
