import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		String streng = "tacocat";
		String anagram = "cocatat";
		System.out.println("Is This An Anagram? " + solve(streng, anagram));

	}

	/*
	 Similar approach to what we did with First non-repeated
	 by using a character array and then post-checking for non 0's
	 */
	private static boolean solve(String s, String a) {	
		if(s.length() != a.length()) {
			return false;
		}
		int CHARCOUNT = 256;
		IWantNull[] characters = new IWantNull[CHARCOUNT];
		for(int i = 0; i < s.length(); i++) {
			char pos = s.charAt(i);
			if(characters[pos] == null) {
				characters[pos] = new IWantNull();
			} else
				characters[pos].count += 1;
		}
		for(int i = 0; i < a.length(); i++) {
			char pos = a.charAt(i);
			if(characters[pos] == null) {
				return false;
			}
			characters[pos].count -= 1;
			if(characters[pos].count < 0) {
				return false;
			}
		}
		for(int i = 0; i < characters.length; i++) {
			if(characters[i] != null && characters[i].count > 0) {
				return false;
			}
		}
		return true;
	}
	
	static class IWantNull {

		public int count = 0;
			
		public IWantNull() {
			count = 1;
		}

	}
}
