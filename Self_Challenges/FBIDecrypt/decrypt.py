# Cheesed this one
# Had the right idea in Java, instead I was adding till all were out of ascii
# range then continually checking by downgrading.

# This is better as it starts at the bottom and builds rather than the top.
# In this case, second was standard between my code along with
# ascii_c and -= second
# The += ascii_c was new as we should tag the original and later
# Subtract it from the next letter, with keeping the previous letter.

# I also didn't realize it was adding the previous ASCII LETTER not
# the entire number, whoops! 
def decrypt(message):
	decoded = ''
	second = 1
	for c in message:
		ascii_c = ord(c)
		ascii_c -= second
		second += ascii_c
		while(ascii_c < ord('a')):
			ascii_c += 26
		decoded += chr(ascii_c)
	return decoded

print(decrypt('dnotq'))
