'''
	Could be improved by removing loss of url by modulous.
	Also glaring detail, having any subsequence with the same letters
	prior will result in the same letter, hence possibility of 
	colliding keys.
'''

import string

from math import ceil

database = {}
urls = ['https://www.youtube.com/feed/history', 'https://leetcode.com/', 'https://www.md5online.org/', 'https://www.md5online.org/']
pieces = 6

def shorten(url):
	if url is None or not url:
		return url
	base = string.digits + string.ascii_lowercase + string.ascii_uppercase
	shortened_url = ""
	partition_size = ceil(len(url) / pieces)
	partition_ptr = 0
	for idx in range(len(url)):
		if idx != 0 and idx % partition_size == 0:
			shortened_url += (base[sum([ord(c) for c in url[partition_ptr:idx]]) % len(base)])	
			partition_ptr = idx
	if url[partition_ptr:]:
		shortened_url += (base[sum([ord(c) for c in url[partition_ptr:idx]]) % len(base)])	
	if shortened_url not in database.keys():
		database[shortened_url] = url
	return shortened_url

def restore(shortened_url):
	if shortened_url is None or not shortened_url:
		return shortened_url
	if shortened_url not in database.keys():
		return None
	return database[shortened_url]

for url in urls:
	shortened = shorten(url)
	restored = restore(shortened)
	print('{} --> {} --> {}'.format(url, shortened, restored))
