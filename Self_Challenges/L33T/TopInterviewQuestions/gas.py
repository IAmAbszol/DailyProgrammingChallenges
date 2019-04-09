def problem(gas, cost):
	total_gas = 0
	starting = 0
	cache = 0
	for i in range(len(gas)):
		total_gas += gas[i]
		total_gas -= cost[i]
		if total_gas < 0:
			total_gas = 0
			start = (i + 1) % len(gas)
		cache += gas[i]
		cache -= cost[i]

	return starting if cache >= 0 else -1 


print(problem([1,2,3,4,5],[3,4,5,1,2]))
print(problem([2,3,4],[3,4,3]))
