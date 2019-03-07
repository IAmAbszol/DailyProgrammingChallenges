import sys
from copy import deepcopy

'''
	8, 0, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15

	[
		2 10 13
		2 3 11
		0 1 9 11
		0 4 6 9 11
		
	]
	...
	Cases
	1. Absolute lowest? Create new list
	2. Middle? Extract sub value less than current, append current to sub, add sub to master, remove anything of equal length
	3. Largest? Append onto all whose tails are less than current
'''

def longest_increasing(arr):
	if arr is None or not arr:
		return arr

	current_longest = 0
	master_list = []
	
	# Iterate through arr
	for elm in arr:
		# Case 1
		if not master_list:
			master_list.append([elm])
			continue
		if all([elm < sub_list[0] for sub_list in master_list]):
			master_list.append([elm])
			if current_longest < len([elm]):
				current_longest = 1
			continue
		# Case 3 - Simple Append
		for sub_list in master_list:
			if sub_list[-1] < elm:
				sub_list.append(elm)
				current_longest = max(current_longest, len(sub_list))
		# Case 2 - Scan each sublist and obtain the middle-ground.
		building_list = []
		for sub_list in master_list:
			tmp_list = []
			for sub_elm in sub_list:
				if elm > sub_elm:
					tmp_list.append(sub_elm)
				else:
					break
			tmp_list.append(elm)
			building_list.append(tmp_list)
			current_longest = max(current_longest, len(tmp_list))
		# Clense the list
		for sub_list in building_list:
			if sub_list in master_list:
				master_list.remove(sub_list)
		
	print(master_list)
	return current_longest

print(longest_increasing([0, 8, 4,12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
