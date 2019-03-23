class BIT:

	def __init__(self, nums):
		self.tree = [ 0 for i in range(len(nums) + 1) ]
		for i, num in enumerate(nums):
			self.update(i + 1, num)

	def update(self, index, value):
		while index < len(self.tree):
			self.tree[index] += value
			index += index & -index
			print(self.tree)

subs = [4,8,1,9,3,5,5,3]

bit = BIT(subs)
bit.update(1, 2)
