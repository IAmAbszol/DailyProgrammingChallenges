# The book has the best solution as its a split method.

'''
	abdecfg
	 ^   
	dbeafcg

'''

def reconstruct(preorder, inorder):
	if preorder is None or inorder is None:
		return None

	if len(preorder) == len(inorder == 1:
		return preorder[0]

	root = preorder[0]
	idx = inorder.index(root)
	
	root.left = reconstruct(preorder[1:1+idx],
							inorder[0:idx])

	root.right = reconstruct(preorder[idx + 1:],
							 inorder[1 + idx:])

	return root
