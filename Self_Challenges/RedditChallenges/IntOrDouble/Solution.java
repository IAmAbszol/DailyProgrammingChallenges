import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		String[] myTestString = {"5242", "52.42", "fifty two"};
		for(int i = 0; i < myTestString.length; i++) {
			System.out.format("Test String: %s is a %s\n", myTestString[i], solve(myTestString[i]));
		}

	}

	private static String solve(String n) {

		try {
			int i = Integer.parseInt(n);
			return "Integer.";
		} catch (Exception e) {
			try {
				double d = Double.parseDouble(n);
				return "Double.";
			} catch (Exception e2) {
				return "Not an int or a double.";
			}
		}

	}

}
