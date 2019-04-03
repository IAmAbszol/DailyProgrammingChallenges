def insert(intervals, interval):
	if not intervals:
		return None
	'''
		[1,3], [6,9]
		[2,5]
		[1,5], [6,9]

		[1,2], [4,5]
		[3,9]
		[1,2], [3,9]
		Process through array
		Start with left of interval = 2
	'''
	final_result = []
	idx = 0
	while idx < len(intervals) and intervals[idx][1] < interval[0]:
		final_result.append(intervals[idx])	
		idx += 1
	# Remove all values that intrude on our interval. Our interval trumps any.
	while idx < len(intervals) and intervals[idx][0] <= interval[1]:
		current_interval = intervals[idx]
		# Interval absolute min, either this or current interval
		interval[0] = min(current_interval[0], interval[0])
		# Interval absolute max, either end or current interval
		interval[1] = max(current_interval[1], interval[1])
		idx += 1
	final_result.append(interval)
	while idx < len(intervals):
		final_result.append(intervals[idx])
		idx += 1
	return final_result

print(insert([[1,3],[6,9]], [2,5]))
