/*
* Node class for a BST to be implemented for the following tree related questions
* on this reddit page.
*/

import java.utils.*;
import java.io.*;

public class Node {
	
	private int value = null;
	private Node left = null;
	private Node right  = null;

	public Node(int value, Node left, Node right) {
		this.value = value;
		this.left = left;
		this.right = right;
	}

	public int getValue() {
		return value;
	}

	public Node getLeft() {
		return left;
	}

	public void setLeft(Node left) {
		this.left = left;
	}

	public Node getRight() {
		return right;
	}

	public void setRight(Node right) {
		this.right = right;
	}

}
