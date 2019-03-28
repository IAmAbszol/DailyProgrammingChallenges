import bisect

class TimeMap:

	def __init__(self):
		self.map = dict()
		self.sorted_keys_cache = None

	def get(self, key):
		value = self.map.get(key)
		if value is not None:
			return value

		if self.sorted_keys_cache is None:
			self.sorted_keys_cache = sorted(self.map.keys())
			print(self.sorted_keys_cache)

		index = bisect.bisect_left(self.sorted_keys_cache, key)

		if index == 0:
			return None
		else:
			return self.map.get(self.sorted_keys_cache[index - 1])

	def set(self, key, value):
		self.sorted_keys_cache = None
		self.map[key] = value

time = TimeMap()
time.set(1, 10)
time.set(3, 15)
time.set(4, 20)
print(time.get(2))
