def solution(arr):
	
	def shortest(p1, p2):
		return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

	shortest_path = 0
	for i in range(len(arr) - 1):
		shortest_path += shortest(arr[i], arr[i + 1])
	return shortest_path

print(solution([(1,1),(3,3),(2,2)]))
print(solution([(0,0),(1,1),(1,2)]))
