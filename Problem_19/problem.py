'''
	N houses, k colors.
	Graphing type of problem in which
	house color cannot neighbor identical colors
'''

def compute(costMatrix, houses, colors):
	
	# Create our cost
	cost = [[0 for i in range(len(costMatrix[0]))] for j in range(len(costMatrix))]

	# Starting cost as any colors from the first house can be chosen
	cost[0] = [i for i in costMatrix[0]]

	# Iterate through houses starting at second level, first level already has potential costs
	for house in range(1, houses):
		for col in range(colors):
			# Select the cost from the two colors chosen for the previous house.
			# Cannot be of same column/color!
			# Python slicing acts as an intersection. Since :0 yields all and col+1: yields 0, 3.
			# Intersection would only grab 0, 3... Strange =/
			previous = cost[house-1][:col] + cost[house-1][col+1:]
			cost[house][col] = costMatrix[house][col] + min(previous)
			print(cost, previous, min(previous))
	return min(cost[-1])

cost=[[4,0,3],[8,3,8],[3,4,4]]
print(compute(cost, 3, 3))
