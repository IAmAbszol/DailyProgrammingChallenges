import java.util.*;
import java.io.*;

public class Problem {
	
	private int[][] map = null;
	private int islands = 0;

	public Problem(int[][] map) {
		this.map = map;
		islands = countIslands();
	}

	public int size() {
		return islands;
	}

	private void dfs(int r, int c, boolean[][] table) {
		if (r < 0 || r >= table.length) {
			return;
		}
		if (c < 0 || c >= table[r].length) {
			return;
		}
		if (table[r][c]) {
			return;
		}
		if (map[r][c] == 0) {
			return;
		}
		table[r][c] = true;
		// Spread out
		dfs(r - 1, c, table);
		dfs(r - 1, c + 1, table);
		dfs(r, c + 1, table);
		dfs(r + 1, c + 1, table);
		dfs(r + 1, c, table);
		dfs(r + 1, c - 1, table);
		dfs(r, c - 1, table);
		dfs(r - 1, c - 1, table);
	}

	private int countIslands() {
		boolean[][] table = new boolean[map.length][map[0].length];
		for (int row = 0; row < table.length; row++) {
			for(int col = 0; col < table[row].length; col++) {
				table[row][col] = false;
			}
		}
		/*
			Scan board
			Every visit, make table as true.
			If map is true, DFS all nearby, increment islands by 1
		*/
		int islands = 0;
		for (int row = 0; row < map.length; row++) {
			for (int col = 0; col < map[row].length; col++) {
				if (map[row][col] == 1 && !table[row][col]){ 
					islands += 1;
					dfs(row, col, table);
				}
			}
		}
	
		return islands;
	}

	public static void main(String[] args) {
		
		int[][] map = new int[6][5];
		map[0] = new int[] { 1, 0, 0, 0, 0 };
		map[1] = new int[] { 0, 0, 1, 1, 0 };
		map[2] = new int[] { 0, 1, 1, 0, 0 };
		map[3] = new int[] { 0, 0, 0, 0, 0 };
		map[4] = new int[] { 1, 1, 0, 0, 1 };
		map[5] = new int[] { 1, 1, 0, 0, 1 };
	
		Problem prob_84 = new Problem(map);	
		System.out.format("%d islands.\n", prob_84.size());

	}

}
