from collections import defaultdict
'''
	Contain a dict that contains all traversed characters.
	Target characters are always positive or 0.
	If 0, that means were on the substring of target character.
	If greater, subtract missing by 1 only if we had landed on that character.
	
	Always subtract element by 1 in dict.
	If missing == 0
		Fast forward left side only for values less than 0
		Compare now, find min.
		Remove left side idx, we know this is target
		Do to zooming, then we add 1 to missing and proceed.
'''
def problem(arr, k):
	
	found_characters = defaultdict(int)
	
	for c in k:
		found_characters[c] += 1

	missing = len(k)
	left_min, right_min = 0, len(arr)
	l_idx, r_idx = 0, 0
	for r_idx, element in enumerate(arr):
		# Check if we landed on a target. Target is never negative.
		if found_characters[element] > 0:
			missing -= 1
		found_characters[element] -= 1
		if not missing:
			# Scan through current array until we reach k.
			while found_characters[arr[l_idx]] < 0:
				found_characters[arr[l_idx]] += 1
				l_idx += 1
			if r_idx - l_idx < right_min - left_min:
				left_min, right_min = l_idx, r_idx
			# k character is never negative, therefore we know this by this spot.
			found_characters[arr[l_idx]] += 1
			missing += 1
			l_idx += 1
	return arr[left_min:right_min + 1] if right_min != len(arr) else ''
		
print(problem('helloabochello', 'abc'))
