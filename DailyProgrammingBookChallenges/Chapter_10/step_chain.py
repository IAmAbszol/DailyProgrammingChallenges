'''
	Add initial word, each each word similar by a character difference, add to queue.
	Continue till we each end by a 1 word difference, empty queue on how we got here.

	Must contain word and path traversed thus far from this word.
	We will need to remove words from the word bank so we don't run into an infinite stack/loop.
'''

from collections import deque
from string import ascii_lowercase

def word_ladder(start, end, words):
	queue = deque([(start, [start])])
	
	while queue:
		print(queue)
		word, path = queue.popleft()

		if word == end:
			return path

		for i in range(len(word)):
			for char in ascii_lowercase:
				modified = word[:i] + char + word[i + 1:]
				if modified in words:
					words.remove(modified)
					queue.append([modified, path + [modified]])
	return None

print(word_ladder('dog', 'cat', ['dog', 'dot', 'dat', 'cat']))
