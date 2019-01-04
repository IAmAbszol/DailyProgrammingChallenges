arr = [1, -1, -5, -3, 3, 4, 2, 8]

# solving =/ preprocess complexity
# optimal
new_arr = []
end = -1
# arrange array
for x in arr:
	if x > 0:
		new_arr.insert(0, x)
		end += 1
	else:
		new_arr.append(x)	

# Proceed with algorithm
for index in range(end+1):
	if new_arr[index] > end:
		continue
	if index > 0:
		new_arr[index-1] = -int(new_arr[index])
	else:
		new_arr[index] = -int(new_arr[index])
	
for index in range(end+1):
	if new_arr[index] > 0:
		print(index+1)
		exit()
print(end+1)
