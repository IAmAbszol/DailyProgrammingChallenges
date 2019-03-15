import java.util.*;
import java.io.*;

public class Problem {

	public int solve(String s) {
		/*
			[)] -> size is 1
			[)(] -> size is 2
		*/
		if (s == null) {
			return -1;
		}
		Stack<String> stack = new Stack<String>();
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == '(') {
				stack.push("" + s.charAt(i));
			}
			if (s.charAt(i) == ')' && !stack.empty()) {
				stack.pop();
			} else if (s.charAt(i) == ')') {
				stack.push("" + s.charAt(i));
			}
		}
		return stack.size();
	}

	public static void main(String[] args) {
		Problem prob_86 = new Problem();
		System.out.format("Requries %d removals to balance.\n", prob_86.solve("()())()"));
		System.out.format("Requries %d removals to balance.\n", prob_86.solve(")("));
	}

}
