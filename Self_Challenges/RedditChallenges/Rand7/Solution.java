import java.io.*;
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		for(int i = 0; i < 25; i++) {
			System.out.print(rand7() + " ");
		}
		System.out.println();

	}

	private static int rand7() {

		/* 
		   Statistically each repeats same number of times
		   hence each all have an equal opportunity to
		   be chosen.		
	  	*/
		int[][] rand7 = {{0,1,2,3,4,5},
						 {6,7,0,1,2,3},
						 {4,5,6,7,0,1},
						 {2,3,4,5,6,7},
					     {0,1,2,3,-1,-1},
						 {4,5,6,7,-1,-1}};

		int result = -1;
		do {
			int row = rand5();
			int col = rand5();
			result = rand7[row][col];
		} while(result == -1);
		return result;
	}

	private static int rand5() {
		return ThreadLocalRandom.current().nextInt(0, 6);
	}

}
