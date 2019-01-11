import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		String input = "The first non repeating character. The very best.";
		System.out.format("Input %s.\nFirst non-repeating character %c\n", input, firstNonRepeatCharacter(input));

	}

	private static char firstNonRepeatCharacter(String n) {
		int CHARCOUNT = 256;
		CountCharacters[] chars = new CountCharacters[CHARCOUNT];
		for(int i = 0; i < n.length(); i++) {
			char pos = n.charAt(i);
			// First occurence
			if(chars[pos] == null) {
				chars[pos] = new CountCharacters(n.charAt(i));
				chars[pos].index = i;
				continue;
			} else
				chars[pos].count += 1;
		}
		for(int i = 0; i < CHARCOUNT; i++) {
			if(chars[i] != null && chars[i].count == 1) {
				return chars[i].character;
			}
		}
		return 0;
	}

	/*
	private static char firstNonRepeatCharacter(String n) {
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		
		// Naive approach, O(n^2) is the worst case
		for(int i = 0; i < n.length(); i++) {
			if(!map.containsKey(n.charAt(i))) {
				map.put(n.charAt(i), 1);
				continue;
			}
			int value = map.get(n.charAt(i));
			map.put(n.charAt(i), value + 1);
		}

		for(int i = 0; i < n.length(); i++) {
			if(map.get(n.charAt(i)) == 1) {
				return n.charAt(i);
			}
		}
		return 0;
	}
	*/
	static class CountCharacters {

		public int index = 0;
		public int count = 1;
		public char character = 0;
		
		public CountCharacters(char c) {
			character = c;
		}	

	}

}
