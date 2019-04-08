class Node:
	
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def reverse(head):
	if not head:
		return head
	if not head.next:
		return head
	print(head.value)
	node = reverse(head.next)
	head.next.next = head
	head.next = None

	return node

head = Node(1, next=Node(2, next=Node(3)))
head = reverse(head)
'''
while head:
	print(head.value)
	head = head.next
'''
