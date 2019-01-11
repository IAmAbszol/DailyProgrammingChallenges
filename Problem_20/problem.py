import random

class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

head_a = Node('1')
head_b = Node('2')

for i in range(10):
	tmp = Node(random.randint(5, 1000))
	tmp.setNextNode(head_a)
	head_a = tmp

	if i % 5 == 0 and i is not 0:
		tmp = Node('0')
		tmp.setNextNode(head_a)
		head_b = tmp
	else:
		tmp = Node(random.randint(5, 10000))
		tmp.setNextNode(head_b)
		head_b = tmp


def find_intersect(head_a, head_b):
	# Who's the culprit? Solve in O(n+m) time
	master_addr = {}

	# Process list A first
	head = head_a
	while head is not None:
		# Value doesn't exist inside dict. Add key following address as value
		if head.getData() not in master_addr:
			master_addr[head.getData()] = id(head)	
		head = head.getNextNode()	

	# Process list b
	head = head_b
	while head is not None:
		if head.getData() in master_addr:
			if master_addr[head.getData()] == id(head):
				return head.getData(), id(head)
		head = head.getNextNode()
	return -1, -1


val, addr = find_intersect(head_a, head_b)
if val == -1:
	print("Found no intersection between lists.")
else:
	print("Found intersection of value {} and Address {}".format(val, addr))






