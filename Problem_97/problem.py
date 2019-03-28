'''
	Set
	parameters (key, value, time)

	Get 
	parameters (key, time)

	An additional constraint is that the problem asks to return CLOSEST time if not present. 

	My thoughts:
		* We need some sort of method to control an array of keys that can is also sorted.
		* This array must actually be sorted since we could use bisect to return the position for the time
		  to be inserted at, then we could just grab the index -1, which would be the "closets". Maybe
		  look at if time - arr[idx - 1] < arr[idx + 1] - time. Meaning which value should we pick, for simplicity
		  I'll just choose the idx -1 .
'''

from bisect import bisect_left
from collections import defaultdict

def TimeMap:
	'''
	def __init__(self):
		self.time_map = {}
		self.cache = None

	def set(self, time, value):
		if cache is not None:
			cache = None
		self.time_map[time] = value

	def get(self, time):
		val = time_map[time]
		if val is notNone:
			return val
		if cache is None:
			cache = sorted(self.time_map.keys())
		idx = bisect_left(cache, time)
		if idx == 0:
			return None
		else:
			return self.time_map.get(self.cache[idx - 1])
	'''

	def __init__(self):
		self.keys = []
		self.values = []

	def set(self, time, value):
		# This is like live sorting instead of constantly destroying our list.
		idx = bisect_left(self.keys, time)
		# If we are at the end, hence we should be placed here.
		if len(self.keys) == idx:
			self.keys.append(time)
			self.values.append(value)
		# We actually found the index.
		elif self.keys[idx] == time:
			self.values[idx] = value
		# Our value doesn't exist but it is able to be placed within the list.
		else:
			self.keys.insert(idx + 1, time)
			self.values.insert(idx + 1, value)

	def get(self, time):
		if not self.keys:
			return None
		idx = bisect_left(self.keys, time)
		if self.keys[idx] == time:
			return self.values[idx]
		elif idx == 0:
			return None
		else:
			return self.values[idx - 1]

def Map:
	
	def __init__(self):
		self.map = defaultdict(TimeMap)

	def set(self, key, time, value):
		self.map[key].set(time, value)
		
	def get(self, key, time):
		time_map = self.map.get(key)
		if time_map is None:
			return None
		return time_map.get(time)	
