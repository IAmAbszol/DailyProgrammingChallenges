import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		String myString = "Sphinx of black quartz, judge my vow";
		System.out.format("String %s : All unique characters (Besides spaces) : %b\n", myString, solve(myString));

		String myAlpha = "abcdefghijk";
		System.out.format("String %s : All unique characters (Besides spaces) : %b\n", myAlpha, solve(myAlpha));
	}

	private static boolean solve(String n) {

		int CHARACTERS = 256;
		int[] counts = new int[CHARACTERS];
		for(int i = 0; i < n.length(); i++) {
			char character = n.charAt(i);
			if(character == ' ') {
				continue;
			}
			counts[character]  += 1;
		}
		for(int i = 0; i < CHARACTERS; i++) {
			if(counts[i] > 1) {
				return false;
			}
		}
		return true;

	}

}
