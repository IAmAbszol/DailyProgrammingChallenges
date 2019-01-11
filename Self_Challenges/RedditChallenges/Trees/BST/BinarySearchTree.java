/*
* Binary Search Tree implementation with basic functionality
* Excluded questions with simple answers
* Excluded
*	- Determines if BST : Traverse through tree, if LHS > Root or RHS < Root, return false
*	- Smallest element in a BST : Traverse far left, if it's a true BST then this is the 
*	  smallest element.
* 	- 2nd Largest element : Traverse far right, return when Root.Right == null. If done recursively,
*	  check for this and return it's value. All preceedings to escape from
*	  recursive statement.
*	- Coordinates : This one looks tricky but really isn't. Take my display algorithm
*	  and proceed with an additional paramter, width or x. Depending on specifications,
*	  it can get a bit harder if the RHS continues off the LHS (Makes sense).
*	  Use a BFS algorithm to do this and an additional class or datastructure to house
*	  1. The Node. 2. The width + depth of each element inside the queue.
*	- Verify Subtree : Start with the either side, I prefer LHS. BFS the LHS and if you experience
*	  null within the first iteration of either LHS or RHS of the node you traversed too, return 
*	  false, if false, proceed with RHS. If that returns false by the same procedure, return false
*	  on the entire function.
*/

import java.util.*;
import java.io.*;

public class BinarySearchTree {

	private Node root;
	private int height = 0;

	public String serializeTree(String key) {
		if(key.contains("pre")) {
			return serializePreorder(root);
		} else
		if(key.contains("in")) {
			return serializeInorder(root);
		} else {
			return "Enter a valid key {\"preorder\", \"inorder\"}";
		}
	}

	/*
	* Root, Left, Right
	* DFS favors these algorithms
	*/
	private String serializePreorder(Node root) {
		if(root == null) {
			return "#";
		}
		return root.getValue() + " " + serializePreorder(root.getLeft()) + " " + serializePreorder(root.getRight());
	}
	
	private String serializeInorder(Node root) {
		if(root == null) {
			return "#";
		}
		return serializeInorder(root.getLeft()) + " " + root.getValue() + " " + serializeInorder(root.getRight());
	}

	public Node deserializeTree(String key, String data) {
		if(key.contains("pre")) {
			return deserializePreorder(root, );
		} else
		if(key.contains("in")) {
			return deserializeInorder(root);
		} else {
			return "Enter a valid key {\"preorder\", \"inorder\"}";
		}
	}

	/*
	* Max Distance of a BST
	*/
	public int maxDistance() {
		// Consider root as farest left
		if(root.getLeft() == null && root.getRight() == null) {
			return 1;
		}
		if(root.getLeft() == null) {
			return maxDepth(root.getRight(), 0);
		} else
		if(root.getRight() == null) {
			return maxDepth(root.getLeft(), 0);
		} else
			return maxDepth(root.getLeft(), 0) + maxDepth(root.getRight(), 0);
	}

	private int maxDepth(Node root, int currentHeight) {
		if(root == null) {
			return currentHeight;
		}
		return Math.max(maxDepth(root.getLeft(), currentHeight + 1), maxDepth(root.getRight(), currentHeight + 1));	
	}

	/*
	* Sum Tree Problem
	* Assumption, if imbalanced/each node must have two children or 
	* none at all else false.
	*/
	public boolean isSumTree() {
		Queue<Node> queue = new LinkedList<>();
		queue.offer(root);
		while(!queue.isEmpty()) {
			Node node = queue.poll();
			if(node.getLeft() == null && node.getRight() == null) {
				continue;
			} else if(node.getLeft() == null || node.getRight() == null) {
				return false;
			}
			if((node.getLeft().getValue() + node.getRight().getValue()) != node.getValue()) {
				return false;
			} else {
				queue.offer(node.getLeft());
				queue.offer(node.getRight());
			}
		}	
		return true;
	}

	/*
	* Binary Search Displays
	*/
	public void displayTreeDFS(Node root) {
		Stack<Node> stack = new Stack<Node>();
		stack.push(root);
		while(!stack.isEmpty()) {
			Node node = stack.pop();
			System.out.print(node.getValue() + " ");
			if(node.getLeft() != null) {
				stack.push(node.getLeft());
			}
			if(node.getRight() != null) {
				stack.push(node.getRight());
			}
		}
		System.out.println();
	}

	// Technically the one below is a BFS as well
	// but traditional BFS uses a Queue
	public void displayTreeBFS(Node root) {
		Queue<Node> queue = new LinkedList<>();
		queue.offer(root);
		while(!queue.isEmpty()) {
			Node node = queue.poll();
			System.out.print(node.getValue() + " ");
			if(node.getLeft() != null) queue.offer(node.getLeft());
			if(node.getRight() != null) queue.offer(node.getRight());
		}
		System.out.println();
	}

	public void displayTree() {
		for(int i = 1; i <= height; i++) {
			displayRecursively(root, i);		
			System.out.println();
		}
	}

	// BFS Implementation
	private void displayRecursively(Node root, int currentHeight) {
		if(root == null) {
			return;
		}
		if(currentHeight == 1) {
			System.out.format("%d ", root.getValue());
		} else if(currentHeight > 1) {
			displayRecursively(root.getLeft(), currentHeight - 1);
			displayRecursively(root.getRight(), currentHeight - 1);
		}
	}

	/*
	* Basic Tree Functions
	*/

	public void delete(int value) {
		root = delete(root, value);
	}

	public Node delete(Node root, int value) {
		if(root == null) {
			return root;
		}
		if(root.getValue() > value) {
			root.setLeft(delete(root.getLeft(), value));
		} else if(root.getValue() < value) {
			root.setRight(delete(root.getRight(), value));
		} else {
			if(root.getLeft() == null) {
				return root.getRight();
			} else if(root.getRight() == null) {
				return root.getLeft();
			}
			
			root.setValue(nextNode(root.getRight()));
			root.setRight(delete(root.getRight(), root.getValue()));
			displayTree();
		}
		
		return root;

	}
	
	private int nextNode(Node root) {
		int value = root.getValue();
		while(root.getLeft() != null) {
			value = root.getLeft().getValue();
			root = root.getLeft();
		}
		
		return value;
	}

	public void insert(int value) {
		root = insert(root, value, 1);
	}

	private Node insert(Node root, int value, int currentHeight) {
		if(root == null) {
			root = new Node(value, null, null);
			if(height != 0) {
				height = Math.max(height, currentHeight);
			} else {
				height = 1;
			}		
			return root;
		}
		if(root.getValue() > value) {
			root.setLeft(insert(root.getLeft(), value, currentHeight + 1));
		} else if(root.getValue() < value) {
			root.setRight(insert(root.getRight(), value, currentHeight + 1));
		}
		return root;
	}

	public Node getRoot() {
		return root;
	}

	public void setRoot(Node root) {
		this.root = root;
	}

	public static void main(String[] args) {
		BinarySearchTree notBST = new BinarySearchTree();
		Node leaf4 = new Node(4, null, null);
		Node leaf5 = new Node(5, null, null);
		Node leaf3 = new Node(3, null, null);
		Node root2 = new Node(2, leaf4, leaf5);
		Node root = new Node(1, root2, leaf3);
		notBST.setRoot(root);
		notBST.displayTreeBFS(root);
		System.out.println(notBST.serializeTree("preorder"));
		System.out.println(notBST.serializeTree("inorder"));
	}

}
