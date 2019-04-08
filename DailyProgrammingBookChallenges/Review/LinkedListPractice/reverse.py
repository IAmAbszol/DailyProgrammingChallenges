class Node:
	
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def reverseBetween(head, n, m):
	
	def swap(prev, cur, i):
		next = cur.next
		cur.next = prev
		if i == 0:
			return cur, next
		return swap(cur, next, i - 1)

	left = None
	n_start = head
	for i in range(1, n):
		left = n_start
		n_start = n_start.next

	m_end, other = swap(left, n_start, m - n)
	if left:
		left.next = m_end
	else:
		head = n_start
	n_start.next = other
	return head

head = Node(1, next=Node(2, next=Node(3, next=Node(4, next=Node(5)))))
head = reverseBetween(head, 2, 4)
while head != None:
	print(head.value)
	head = head.next
