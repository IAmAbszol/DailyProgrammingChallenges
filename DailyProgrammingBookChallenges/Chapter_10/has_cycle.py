'''
	One way of doing this is through DFS, kind of like I did in Problem 91? or 90.

	To find a cycle, start at some point traverse through, either having a list containing if its within
	or having a list of boolean checks of visited. If any are visited, then we have a cycle.

	This solution in the book uses a DFS approach coupled with basic looping to visit all neighbors.
'''

def search(graph, vertex, visited, parent):
	visited[vertex] = True

	# DFS approach, iterate through neighbors and span till we visited
	for neighbor in graph[vertex]:
		if not visited[neighbor]:
			if search(graph, neighbor, visited, vertex):
				return True
		# Somewhere else we cycled
		elif parent != neighbor:
			return True

	return False

def has_cycle(graph):
	# Create list that contains visited locations/verticies
	visited = {v: False for v in graph.keys()}
	
	# Check each vertex, check for cycle
	for vertex in graph.keys():
		if not visited[vertex]:
			if search(graph, vertex, visited, None):
				return True

	return False
