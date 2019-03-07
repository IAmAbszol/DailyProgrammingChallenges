import java.util.*;
import java.io.*;

public class Problem {

	public int[] smallestMissing(int[] arr) {
		if (arr == null) {
			return null;
		}
		if (arr.length < 2) {
			return null; 
		}
		int smallest = Integer.MAX_VALUE;
		int second_smallest = Integer.MAX_VALUE;	
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] < smallest) {
				second_smallest = smallest;
				smallest = arr[i];
			}
		}
		return new int[] { smallest, second_smallest };
	}

	public static void main(String[] args) {
		int[] arr = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 };
		Problem prob = new Problem();
		int[] result = prob.smallestMissing(arr);
		System.out.println(result[0] + ", " + result[1]);
	}

}
