class Node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# Leet code solution, queue was pretty sick.
# Need more practice in linked lists.
def partition(node, x):
	smallerHead = Node(0)
	greaterHead = Node(0)
	smallerLast = smallerHead
	greaterLast = greaterHead
	while node:
		if node.value < x:
			smallerLast.next = node
			smallerLast = smallerLast.next
		else:
			greaterLast.next = node
			greaterLast = greaterLast.next
		node = node.next
	greaterLast.next = None
	smallerLast.next = greaterHead.next
	return smallerHead.next

root = Node(1, next=Node(4, next=Node(3, next=Node(2, next=Node(5, next=Node(2))))))
ret = partition(root, 3)
while ret != None:
	print(ret.value)
	ret = ret.next
