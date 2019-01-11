import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		String[] myTestStrings = { "tacocat", "anna", "bob", "chuck" };
		for(int i = 0; i < myTestStrings.length; i++) {
			System.out.println("Test String: " + myTestStrings[i] + "'s shortest palindrome is " + solve(myTestStrings[i]));
		}

	}

	private static String solve(String str) {

		if(str == null || str.length() <= 1) {
			return str;
		}
	
		int pos = str.length()/2;
		if(pos % 2 == 0) {
			pos--;
		}
		String developing = "";
		for(int i = pos; i >= 0; i--) {
			if(str.charAt(i) == str.charAt(str.length() - i - 1)) {
				if(i != (str.length() - i - 1)) {
					developing = str.charAt(i) + developing + str.charAt(str.length() - i - 1);
					return developing; 
				} else
					developing = "" + str.charAt(i);
			}
		}
		return "Nothing.";
	
	}

}
