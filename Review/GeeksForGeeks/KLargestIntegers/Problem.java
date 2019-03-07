import java.util.*;
import java.io.*;

public class Problem {

	public int[] kLargest(int[] arr, int k) {
		/*
		 * 9, 1, 5, 10, 14, 3, 2 --> k = 3 --> 9,10,14
		 * [Smallest ... Highest] = k
		 * [MIN, MIN, MIN] --> Arrays.fill(arr, Integer.MIN_VALUE)
		 * [MIN, MIN, 9]
		 * [MIN, 1, 9]
		 * [1,5,9]
		 * [5,9,10]
		 * [9,10,14]
			--> Runtime O(nk) 
		 */
		if (arr == null || k > arr.length) {
			return null;
		}
		int[] k_arr = new int[k];
		Arrays.fill(k_arr, Integer.MIN_VALUE);
		for (int i = 0; i < arr.length; i++) {
			// Problem if our temp value was -1 when inserting o.O
			int temp = -1;
			for (int j = k_arr.length - 1; j >= 0; j--) {
				if (arr[i] > k_arr[j] && temp == -1) {
					temp = k_arr[j];
					k_arr[j] = arr[i];
				} else if (temp != -1) {
					int temp2 = k_arr[j];
					k_arr[j] = temp;
					temp = temp2;
				}
			}
		}
		return k_arr;
	}

	public static void main(String[] args) {
		int[] arr = { 9, 1, 5, 10, 14, 3, 2 };
		Problem prob = new Problem();
		int[] result = prob.kLargest(arr, 3);
		for (int i = 0; i < result.length; i++) {
			System.out.println(result[i]);
		}
	}

}
