def number_of_steps(steps):
	array = [1] * steps
	return helper(array)

def number_of_steps2(steps):
	array = [1] * steps
	return helper2(array)

# 1 and 2 steps	
def helper(array):
	if len(array) <= 1:
		return 1
	total = 0
	total += helper(array[2:])
	total += helper(array[1:])
	return total

# 1, 3, and 5 steps
def helper2(array):
	if len(array) <= 1:
		return 1
	total = 0
	if len(array) - 5 >= 0:
		total += helper2(array[5:])
	if len(array) - 3 >= 0:
		total += helper2(array[3:])
	total += helper2(array[1:])
	return total

print(number_of_steps(4))
print(number_of_steps2(4))
