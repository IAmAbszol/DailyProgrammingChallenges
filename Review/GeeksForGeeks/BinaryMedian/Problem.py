import java.util.*;
import java.io.*;

class Problem {

	public double compute_median(int[] x, int[] y) {
		if (x == null || y == null) {
			return -1;
		}
		/*
			1, 12, 15, 26, 38
			2, 13, 17, 30, 45
			length = 10
			so.. mid = 5 or idx = 4
			ptr = 0, onX = true if x[0] < y[0] else false
			1
			12 --> Nope, swap --> 2
			13 --> Nope, swap --> 12
			15 --> Nope, swap --> 13
			17 --> Nope, swap --> 15 --\ = 16, ans
			26 --> Nope, swap --> 17 --/
		*/
	}

	public static void main(String[] args) {
		
	}

}

