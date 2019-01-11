import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) {

		char[] characters = {'A', 'B', 'C', 'D'};
		System.out.println("Creating Bejeweled Board by 2 Methods");
		createBoard(characters, 8, 8);		

	}

	private static void createBoard(char[] pieces, int width, int height) {
		char[][] board = constantCheckMethod(pieces, width, height);
		for(int row = 0; row < height; row++) {
			for(int col = 0; col < width; col++) {
				System.out.print(board[row][col] + " ");
			}	
			System.out.println();
		}
		board = dpMethod(pieces, width, height);
		for(int row = 0; row < height; row++) {
			for(int col = 0; col < width; col++) {
				System.out.print(pieces[board[row][col]] + " ");
			}	
			System.out.println();
		}
	}

	private static char[][] dpMethod(char[] pieces, int width, int height) {
		char[][] board = new char[height][width];
		for(int row = 0; row < height; row++) {
			for(int col = 0; col < width; col++) {
				while(true) {
					// Case 1. Empty block, only happens on first column iteration of row 0, thus start.
					if(board[row][col] == "\u0000") {
						board[row][col] = rand(pieces);
						board[row][col + 1] = int(board[row][col]) + pieces.length;
						board[row + 1][col] = int(board[row][col]) + pieces.length;
						break;
					}
					int piece = rand(pieces);
					// Case 2. Block wasn't empty, we have to figure out what group it belongs too.
					// First figure out index.
					if(board[row][col] % pieces.length == piece) {
						// Piece matches our piece. Now how much have we done so far?
						if(modCount(board[row][col], piece) >= 2) {
							// Placing piece completes a row of 3.
							continue;
						} 
						// Placing piece is fine
						board[row][col] = piece;
						// Distribute
						if(col < (width - 1)) {
							board[row][col + 1] = board[row][col] + pieces.length;
						}
						if(row < (height - 1)) {
							board[row + 1][col] = board[row][col] + pieces.length;
						}
						break;
					}
					// Case 3. Our new piece doesn't match the piece previously placed.
					// Only check is above one piece.
					if(row > 0) {
						if(board[row - 1][col] % pieces.length == piece) {
							// Piece matches our piece. How much has that done so far?
							if(modCount(board[row][col], piece) >= 2) {
								// Placing piece completes a row of 3
								continue;
							}
							board[row][col] = piece;
							if(col < (width - 1)) {
								board[row][col + 1] = board[row][col] + pieces.length;
							}
							if(row < (height - 1)) {
								board[row + 1][col] = board[row][col] + pieces.length;
							}
							break;
						} 
					} else {
						board[row][col] = piece;
						if(col < (width - 1)) {
							board[row][col + 1] = board[row][col] + pieces.length;
						}
						board[row + 1][col] = board[row][col] + pieces.length;
						break;
					}
				}
			}
		}
	}

	private static int modCount(int n, int d) {
		int counter = 0;
		while(n > d) {
			n -= d;
			counter += 1;
		}
		return counter;
	}

	/*
	* Naive, bad approach.
	* Checking like this is... distasteful =O
	*/
	private static char[][] constantCheckMethod(char[] pieces, int width, int height) {
		char[][] board = new char[height][width];
		for(int row = 0; row < height; row++) {
			for(int col = 0; col < width; col++) {
				while(true) {
					board[row][col] = pieces[rand(pieces)];
					// check surrounding area
					if(row >= 2 && board[row - 1][col] == board[row - 2][col] && board[row][col] == board[row - 1][col]) {
						continue;
					}
					if(row < (height - 2) && board[row + 1][col] == board[row + 2][col] && board[row][col] == board[row + 1][col]) {
						continue;
					}
					if(col >= 2 && board[row][col - 1] == board[row][col - 2] && board[row][col] == board[row][col - 1]) {
						continue;
					}
					if(col < (width - 2) && board[row][col + 1] == board[row][col + 2] && board[row][col] == board[row][col + 1]) {
						continue;
					}
					break;
				}
			}
		}
		return board;
	}

	private static int rand(char[] pieces) {
		return new Random().nextInt(pieces.length);
	}

}
