import java.io.*;
import java.util.*;

class Problem {

	public int timesAppeared(int n, int x) {
		if (n < 1) {
			return -1;
		}
		int[][] multiplicationTable = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				multiplicationTable[i][j] = (i + 1) * (j + 1);
				System.out.print(multiplicationTable[i][j] + " ");
			}
			System.out.println();
		}
		int count = 0;
		for (int i = 1; i < (n + 1); i++) {
			if (x % i == 0 && (x / i) <= n) {
				count += 1;
			}
		}
		return count;
	}

	public static void main(String[] args) {
		Problem prob = new Problem();
		System.out.println(prob.timesAppeared(6, 12));
	}

}
