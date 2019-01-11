import java.util.*;
import java.io.*;

public class LCS {

	public static void main(String[] args) {
	
		char[] X = {'A','B','C','A','B'};
		char[] Y=  {'G','H','Z','B','C','A'};
		// count should print 3 as X[1:4] == Y[3:6]
		System.out.println(lcs(X, Y, X.length - 1, Y.length - 1, 0, ""));

	}

	private static int lcs(char[] X, char[] Y, int x, int y, int count, String subString) {
		// Case 0: If either hit the end, return the one
		if(x == 0 || y == 0) {
			return count;
		}

		// Case 1: They match, increment count and move downwards
		if(X[x] == Y[y]) {
			count = lcs(X, Y, x - 1, y - 1, count + 1, subString);
		}
		
		// Case 2, neither matched, we need to account for
		// us being on this count or moving down separate trees
		return Math.max(count, Math.max(lcs(X, Y, x - 1, y, 0, subString), lcs(X, Y, x, y - 1, 0, subString)));

	}

}
