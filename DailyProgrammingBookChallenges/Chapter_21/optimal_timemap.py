import bisect

from collections import defaultdict

class MultiTimeMap:
	
	def __init__(self):
		self.map = defaultdict(TimeMap)

	def set(self, key, time, value):
		self.map[key].set(time, value)
	
	def get(self, key, time):
		time = self.map.get(key)
		if time is None:
			return None
		return self.map.get(time)

class TimeMap:

	def __init__(self):
		self.keys = []
		self.values = []

	def set(self, time, value):
		
		idx = bisect.bisect_left(self.keys, time):
		if len(self.keys) == 0 and idx == 0:
			self.keys.append(time)
			self.values.append(value)
		elif self.keys[idx] == time:
			self.values[idx] = value
		else:
			self.keys.insert(idx + 1, time)
			self.values.insert(idx + 1, value)

	def get(self, time):
		value = self.map.get(time)
		if value is not None:
			return value
		idx = bisect.bisect_left(self.keys, time)
		if idx == 0:
			return None
		
		return self.values[idx - 1]
