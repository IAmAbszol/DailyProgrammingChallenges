import java.util.*;
import java.io.*;

public class QueensProblem {

	private static int count = 0;

	public static void main(String[] args) {

		// keep it simple with 4x4 board size and 4 queens.
		char[][] input = new char[8][8];	
		solve(input, 8);
	}

	private static void solve(char[][] input, int queens) {


		for(int row = 0; row < input.length; row++) {
			for(int col = 0; col < input[row].length; col++) {
				input[row][col] = '.';
			}
		}

		if(placeQueen(input, 1, 0, 0, queens)) {
			display(input);
		} else {
			System.out.println("No solution.");
		}

	}

	private static boolean placeQueen(char[][] input, int queenNumber, int row, int col, int queens) {

		if(queenNumber > queens) {
			return true;
		}

		for(int i = 0; i < input.length; i++) {
			input[row][i] = 'Q';
			if(goodMove(input, queenNumber)) {
				if(placeQueen(input, queenNumber + 1, row + 1, 0, queens)) {
					return true;
				}
			}
			input[row][i] = '.';	
		}

		return false;

	}
/*
	private static boolean placeQueen(char[][] input, int queenNumber, int row, int col, int queens) {
		if(col > 0) {
			input[row][col-1] = '.';
		}
		// We exceeded our placement, move up a level
		if(col >= input[0].length) {
			return false;
		}
		input[row][col] = 'Q';
		
		
		if(goodMove(input, queenNumber)) {
			if(queenNumber >= queens) {
				return true;
			}
			// Column returned false, exhuasted top stack attempt
			if(!placeQueen(input, queenNumber + 1, queenNumber, 0, queens)) {
				if(!goodMove(input, queenNumber)) {
					input[row][col] = '.';
					placeQueen(input, queenNumber, row, col + 1, queens); 
				}
			} else {
				return true;
			}
		}
		return placeQueen(input, queenNumber, row, col + 1, queens);
	}
*/
	// Use basic board recursion view, indicies indicate unique positions for queen to cover within.
	private static boolean goodMove(char[][] input, int queens) {
		Set<Integer> rowWithQueens = new HashSet<Integer>();
		Set<Integer> columnWithQueens = new HashSet<Integer>();
		Set<Integer> northEastDiagonalWithQueens = new HashSet<Integer>();
		Set<Integer> southEastDiagonalWithQueens = new HashSet<Integer>();	
		for(int row = 0; row < input.length; row++) {
			for(int col = 0; col < input[row].length; col++) {
				if(input[row][col] == 'Q') {
					rowWithQueens.add(row);
					columnWithQueens.add(col);
					northEastDiagonalWithQueens.add(row + col);
					southEastDiagonalWithQueens.add(queens - 1 - row + col);
				}
			}
		}
		
		int total = queens - rowWithQueens.size();
		total += queens - columnWithQueens.size();
		total += queens - northEastDiagonalWithQueens.size();
		total += queens - southEastDiagonalWithQueens.size();
		if(total == 0) {
			return true;
		}
		return false;
	}

	private static void display(char[][] input) {
		for(int row = 0; row < input.length; row++) {
			for(int col = 0; col < input[row].length; col++) {
				System.out.print(input[row][col] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}

}
