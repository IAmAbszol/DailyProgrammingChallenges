import java.util.*;
import java.io.*;

public class Problem {

	Tree myTree = null;

	public Problem() {
		Node na = new Node('a', new Node('b', new Node('d', null, null), null), new Node('c', null, null));
		myTree = new Tree(na);
	}

	public int deepest() {
		return deepest(myTree.root, 1);
	}
	
	private int deepest(Node node, int level) {
		if (node == null) {
			return level - 1;
		}
		int currentMax = 0;
		currentMax = Math.max(currentMax, deepest(node.left, level + 1));
		currentMax = Math.max(currentMax, deepest(node.right, level + 1));
		System.out.format("%d for current level and %d for currentMax\n", level, currentMax);	
		return currentMax;
	}

	public static void main(String[] args) {

		Problem prob = new Problem();
		System.out.println(prob.deepest());

	}

	class Node {
		
		char val;
		Node left = null;
		Node right = null;

		public Node(char val, Node left, Node right) {
			this.val = val;
			this.left = left;
			this.right = right;
		}

	}

	class Tree {
		
		Node root = null;
		int numberOfNodes = 0;
	
		public Tree(Node root) {
			this.root = root;
		}

	}

}
