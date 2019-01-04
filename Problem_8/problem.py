my_list = [2,4,6,2,5]
my_list2 = [5,1,1,5]

def find_max(data):
	if len(data) == 1:	
		return data[0]
	if len(data) == 2:
		return max(data)
	return max(data[0] + find_max(data[2:]), find_max(data[1:]))

print(find_max(my_list)) 
print(find_max(my_list2))
