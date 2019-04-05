def problem(arr):
	prev = arr[0] - 1
	in_dupes = False
	length = 0
	for i in range(len(arr)):
		if prev == arr[i]:
			if in_dupes:
				continue
			length += 1
			in_dupes = True
		else:
			in_dupes = False
			prev = arr[i]
			length += 1
	return length

print(problem([0,0,1,1,1,1,1,2,3,3]))
	
