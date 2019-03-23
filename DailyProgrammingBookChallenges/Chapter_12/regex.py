def matches_first_char(s, r):
	return s[0] == r[0] or (r[0] == '.' and len(s) > 0)

def matches(s, r):
	
	# Base case, if both are blank
	if r == '':
		return s == ''

	# Second case, if theres one character left or its not * for the next character
	if len(r) == 1 or r[1] != '*':
		if matches_first_char(s,r):
			return matches(s[1:], r[1:])
		else:
			return False
	
	else:
		# If there was a * character
		if matches(s, r[2:]):
			return True
		
		# Didn't match, probably as suffixes after.
		i = 0
		while matches_first_char(s[i:], r):
			if matches(s[i + 1:], r[2:]):
				return True
			i += 1

print(matches('Hello', 'He*o'))
