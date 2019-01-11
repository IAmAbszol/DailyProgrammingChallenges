import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	private void justifyString(String[] input, int maxWidth) {

		/*
		* Compute cost matrix
		*/
		int[][] costMatrix = new int[input.length][input.length];
		for(int row = 0; row < costMatrix.length; row++) {
			costMatrix[row][row] = maxWidth - input[row].length(); 
			for(int col = row+1; col < costMatrix[row].length; col++) {
				costMatrix[row][col] = costMatrix[row][col-1] - input[col].length() - 1;
			}
		}

		for(int row = 0; row < costMatrix.length; row++) {
			for(int col = 0; col < costMatrix[row].length; col++) {
				if(costMatrix[row][col] < 0) {
					costMatrix[row][col] = Integer.MAX_VALUE;
					continue;
				}
				costMatrix[row][col] = (int)Math.pow(costMatrix[row][col], 2);
			}
		}

		/*
		* Compute cost vs break matricies
		* Calculation goes
		* min(costMatrix[i][j-1] + cost[j]) --> j becomes breaks key ie
		* computing breaks is from index to less than that value.
		*/
		int[] cost = new int[input.length];
		int[] breaks = new int[input.length];
		for(int i = input.length - 1; i >= 0; i--) {
			cost[i] = costMatrix[i][input.length - 1];
			breaks[i] = input.length;
			for(int j = input.length - 1; j > i; j--) {
				if(costMatrix[i][j-1] == Integer.MAX_VALUE) {
					continue;
				}
				int compute = costMatrix[i][j-1] + cost[j];
				if(cost[i] > compute) {
					cost[i] = compute;
					breaks[i] = j;
				}
			}
		}

		int i = 0;
		int j = 0;
		StringBuilder sb = new StringBuilder();
		while(j < breaks.length) {
			j = breaks[i];
			for(int k = i; k < j; k++) {
				sb.append(input[k] + " ");
			}
			sb.append("\n");
			i = j;
		}	
		System.out.println(sb.toString());
	}

	public static void main(String[] args) {
//		String[] inputString = {"Kyle", "enjoys", "coding","daily","and","having","fun"};
		String[] inputString = {"Miah", "eats", "chipotle."};
		Solution solution = new Solution();
		solution.justifyString(inputString, 10);	
	}

}
