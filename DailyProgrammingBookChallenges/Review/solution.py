from collections import defaultdict

def problem(arr, compare):
	char_count = defaultdict(int)

	for c in compare:
		char_count[c] += 1

	missing = len(compare)
	min_left, min_right = 0, len(arr)
	l_idx = 0

	for r_idx, element in enumerate(arr):
		if char_count[element] > 0:
			missing -= 1
		char_count[element] -= 1
		print(element, char_count)
		if missing == 0:
			while char_count[arr[l_idx]] < 0:
				char_count[arr[l_idx]] += 1
				l_idx += 1
			if r_idx - l_idx < min_right - min_left:
				min_left, min_right = l_idx, r_idx

			char_count[arr[l_idx]] += 1
			missing += 1
			l_idx += 1
	print(char_count)
	return arr[min_left:min_right + 1] if min_right != len(arr) else ''

print(problem('aoooobchabc', 'abc'))
	
