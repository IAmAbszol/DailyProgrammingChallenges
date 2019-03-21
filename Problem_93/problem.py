'''
	This problem actually stumped me.
	
	Going ahead and trying my solution would've yielded an incorrect answer, here's what I came up with.

	Queue a breadth search that contains a tuple 
	tuple would be value, level, bst_level

	Place root into breadth

	Loop
		root = breadth.get()
		if check requirements
			overall = max(current, overall)
		
		
		
				10
		12				20
	5		14		3		10
0		6 7		15

queue
(3, 3, 0), (10, 3, 0), (0, 3, 2), (6, 3, 2)

X Conflicts with BST onto otherside, would require more info
	
Using Largest BST in Binary Tree from Tushar Roy

				
				10
		12				20
	5		14		3		10
0		6 7		15

	1. Perform a post order traversal
		Left, Right, Root
		
		Left -> 0, BST (T, 1, 0, 0)
		Right -> 6, BST (T, 1, 0, 0)
		Root -> LHS is BST and RHS is BST. Max of LHS < Root and Min of RHS > Root
				(T, LHS Nodes + RHS Nodes + 1, min of LHS, max of RHS)
	2. Return, continue


	Complete flow

	Base case, if LHS and RHS is none, just truth True, 1 node, min value, max value (values))
	
	Evaluate LHS and evaluate RHS

	Once root, is our LHS and RHS true? Is our LHS max < us and RHS min > us if so, return true add one to lhs + rhs.

'''

import sys

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def solution(tree):
	return largest_bst(tree, 0)[4]

def largest_bst(tree, best):

	# Base recursion case
	if tree.left is None and tree.right is None:
		return (True, 1, tree.value, tree.value, 1)

	# Perform post order, evaluate far left and right
	lhs_truth, lhs_nodes, lhs_min, lhs_max, lhs_best = largest_bst(tree.left, best) if tree.left is not None else (True, 0, 0, 0, 0)
	
	rhs_truth, rhs_nodes, rhs_min, rhs_max, rhs_best = largest_bst(tree.right, best) if tree.right is not None else (True, 0, 0, 0, 0)

	# Check if it's valid BST
	if lhs_truth and lhs_max < tree.value and rhs_truth and rhs_min > tree.value:
		return (True, 1 + lhs_nodes + rhs_nodes, lhs_min, rhs_max, max(best, 1 + lhs_nodes + rhs_nodes, rhs_best, lhs_best))
	else:
		return (False, 1, 0, 0, max(1, best, lhs_best, rhs_best))

root = Node(25, left=Node(18, left=Node(19, right=Node(15)), right=Node(20, left=Node(18), right=Node(25))), right=Node(50, left=Node(35, left=Node(20, right=Node(25)), right=Node(40)), right=Node(60, left=Node(55), right=Node(70))))

print(solution(root)) 
