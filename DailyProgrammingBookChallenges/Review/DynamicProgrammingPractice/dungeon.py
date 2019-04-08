'''
	This problem can be manipulated in such a way we can represent it as the
	Unique_paths problem.

	Our valiant knight must stay above 0, we calculate the minimum health needed
	to traverse this dangerous task. He can also only move down and to the right.

	-2	-3	3
	-5	-10	1
	10	30	-5

	Tweak: Manipulate the base pick of our dp solution to choose values
	whose sums paired with current square results in the closest value to 0 but 
	not 0.

	-2	-5	-2
	-7	-15	-1
	3	15	10 	X
	
	Idea: Instead of computing the sum totals of travesal from top to bottom,
	lets do bottom up. This will give us the absolute minimum.
	We still check bottom and right for mins then subtract our current position but
	then we take the max between 1 and that as we can't have any negatives.

	6	4	2
	6	1	5
	1	1	6 <-- 1 - (-5) since 1 is for staying about 1 hp.

'''

def dungeon(knight_map):

	r = len(knight_map)
	c = len(knight_map[0])

	dp = [[0 for _ in range(c)] for __ in range(r)]

	# Compute bottom right as initial
	dp[-1][-1] = max(1, 1 - knight_map[-1][-1])

	# Traverse backwards [::-1] does so
	for i in range(r)[::-1]:
		for j in range(c)[::-1]:
			# Compute minimum between the two positions, If none exist (Edge) then 1.
			minimum = min([dp[y][x] for y, x in ((i + 1, j), (i, j + 1)) if x < c and y < r] or [1])
			# Compute the max between 1 and the current - map
			dp[i][j] = max(1, minimum - knight_map[i][j])
	return dp[0][0]

print(dungeon([[-2,-3,3],[-5,-10,1],[10,30,-5]]))



