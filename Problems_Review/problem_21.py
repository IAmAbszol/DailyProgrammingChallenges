def problem(arr):
	if arr is None:
		return arr

	start = [ a[0] for a in arr ]
	end = [ a[1] for a in arr ]
	start.sort()
	end.sort()

	rooms = 0
	start_ptr = 0
	end_ptr = 0
	
	while start_ptr < len(arr):
		if start[start_ptr] <= end[end_ptr]:
			rooms += 1
			start_ptr += 1
		elif start[start_ptr] > end[end_ptr]:
			rooms -= 1
			end_ptr += 1
		if end_ptr >= len(arr):
			end_ptr = len(arr) - 1
	return rooms

intervals = [ (30, 75), (0, 50), (60, 150) ]
print(problem(intervals))
