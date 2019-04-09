'''
	aab
	Parent		Child
	a | ab	->	a|b
				ab|
	aa | b
	aab|

	Each step, check if s == s[::-1]
'''

def partition(start, string, tmp=[], res=[]):
	# Start is at the end of string, single character.
	if start >= len(string):
		res.append(tmp)
		return
	for i in range(start, len(string)):
		sub = string[start:i+1]
		if sub == sub[::-1]:
			partition(i + 1, string, tmp + [sub], res)
	return res

print(partition(0, 'aab'))
