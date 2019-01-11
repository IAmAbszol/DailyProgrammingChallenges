import java.io.*;
import java.util.*;

public class Solution {

	private static HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

	public static void main(String[] args) {
		System.out.println("Iteratively");
		for(int i = 0; i < 6; i++) {
			System.out.print(iteratively(i) + " ");
		}
		System.out.println();

		System.out.println("Recursively");
		for(int i = 0; i < 6; i++) {
			System.out.print(recursively(i) + " ");
		}
		System.out.println();
	
		System.out.println("BONUS! Dynammic Programming =D");
		for(int i = 0; i < 6; i++) {
			System.out.print(dp(i) + " ");
		}
		System.out.println();
	}

	private static int dp(int n) {
		if(map.containsKey(n)) {
			return map.get(n);
		}
		int f = 0;
		if(n <= 2) {
			f = 1;
			if(n == 0) f = 0;
		} else {
			f = dp(n - 1) + dp(n - 2);
		}
		map.put(n, f);
		return f;
	}

	private static int recursively(int n) {
		if(n <= 1) {
			return n;
		}
		return recursively(n-1) + recursively(n-2);
	}

	private static int iteratively(int n) {
		if(n < 1) {
			return n;
		}
		int prev = 0, cur = 1;
		for(int i = 1; i < n; i++) {
			int tmp = cur;
			cur	+= prev;
			prev = tmp;
		}
		return cur;
	}

}
