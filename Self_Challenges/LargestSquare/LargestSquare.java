import java.util.*;
import java.io.*;

public class LargestSquare {

	public static void main(String[] args) {

		int[][] grid = {{0,0,1,1,1,0,0,1,1},{1,1,1,1,1,0,0,1,1},{1,1,1,1,1,0,0,0,0},{0,0,0,0,0,0,0,0,0}};
		System.out.println("Largest Square is " + solve(grid));

	}

	private static int solve(int[][] grid) {

		/*
		* Solving without using new array, constant space held.
		*/
		for(int i = 0; i < (grid.length - 1); i++) {
			for(int j = 0; j < (grid[i].length - 1); j++) {
				int span = Math.min(grid[i][j], grid[i+1][j]);
				span = Math.min(span, grid[i][j+1]);
				grid[i+1][j+1] += span;
			}
		}
		int max = 0;
		for(int i = 0; i < grid.length; i++) {
			for(int j = 0; j <  grid[i].length; j++) {
				if(grid[i][j] > max) {
					max = grid[i][j];
				}
			}
		}
		return max;
	}

}
