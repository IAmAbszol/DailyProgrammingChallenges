import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		System.out.println("Permutations of CAT are:");
		solve("CAT", 0, 2);

	}

	private static void solve(String s, int left, int right) {
		
		if(left == right) {
			System.out.println(s);
			return;
		}

		for(int i = left; i <= right; i++) {
			s= swap(s, left, i);
			solve(s, left+1, right);
			s = swap(s, left, i);
		}

	}

	private static String swap(String s, int i, int j) {
		char[] characters = s.toCharArray();
		char tmp = characters[i];
		characters[i] = characters[j];
		characters[j] = tmp;
		return String.valueOf(characters);
	}

}
