'''
	Hello 12.35
	1 --> base * val + 1
	12 --> 10 * 1 + 2 => 12
	1235, power = 2	
	
'''
def parseDouble(s):
	if s is None:
		return s

	val = 0
	base = 10
	power = 0
	is_power = False
	pos = 0

	while pos < len(s):
		if s[pos].isdigit():
			break
		pos += 1

	while pos < len(s):
		if s[pos] == '.':
			pos += 1
			is_power = True
			continue
		val = val * base + int(s[pos])
		if is_power:
			power += 1
		pos += 1

	return val / (10 ** power)

print(parseDouble('Hello 12.35'))
