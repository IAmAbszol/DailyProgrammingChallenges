def is_palindrome(word):
	return word == word[::-1]

def palindrome(words):
	result = []

	for idx, word1 in enumerate(words):
		for idx2, word2 in enumerate(words):
			if idx == idx2:
				continue
			if is_palidnrome(word1 + word):
				result.append((idx, idx2))
	return result
