'''
	solution.py
	Second test I wasn't sure on the return as if 
	it is to return two lists for
	'bed','bath'....
	and
	'bedbath'....
	If so, in the return, recurse solve
'''

def solve(word_bank, sentence, i, j):
	if ' ' in sentence:
		return None

	words = []
	previous = ""
	while j <= len(sentence):
		if sentence[i:j] in word_bank:
			words.append(sentence[i:j])
			# Start new segment
			words.extend(solve(word_bank, sentence, j, j+1))	

		j += 1
	return list(set(words))

data = [((["quick","brown","fox","the"], "thequickbrownfox"), ["the","quick","brown","fox"]),
		((["bed","bath","bedbath","and","beyond"], "bedbathandbeyond"), ["bed","bath","bedbath","and","beyond"])]
	
	
for [case, expected] in data:
	print(solve(case[0], case[1], 0, 0))

