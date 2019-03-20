from collections import defaultdict

def cuts(wall):
	if wall is None:
		return wall

	cut = defaultdict(int)
	for row in wall:
		length = 0
		for elm in row[:-1]:
			length += elm
			cut[length] += 1
	print(cut)
	return len(wall) - max(cut.values())

wall = [[3,5,1,1],[2,3,3,2],[5,5],[4,4,2],[1,3,3,3],[1,1,6,1,1]]
print(cuts(wall))
