import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) {

		int[] input = {0,1,10,4,2,5,9,8,6};
		int sum = 20;

		int[] solved = solve(input, sum);
		if(solved == null) {
			System.out.println("No solution!");
		}
		for(int i = 0; i < solved.length; i++) {
			System.out.print(solved[i] + " ");
		}
		System.out.println();

	}

	/*
		Choose two points, lets say i and jith being starting points.
		From there, analyze entire array.

		Nothing? No worries
		Move j up and continue

		Burned out j? maybe i is the problem.
		We know that the first is completely exhuasted, complete iteration of jith
		Still nothing?
		2nd is burned out, iterate till solution
	*/
	private static int[] solve(int[] arr, int k) {

		if(arr.length < 4) {
			return arr;
		}

		Arrays.sort(arr);

		// Choose 2 points using i and j
		for(int i = 0; i < arr.length; i++) {
			for(int j = i + 1; j < arr.length; j++) {
				int left = k - (arr[i] + arr[j]);
				int low = j + 1;
				int high = arr.length - 1;
				while(low < high) {
					int sum = arr[low] + arr[high];
					if((left - sum) > 0) {
						low++;
						continue;
					}
					if((left - sum) < 0) {
						high--;
						continue;
					}
					return new int[]{arr[i], arr[j], arr[low], arr[high]};
				}
			}
		}
		return null;

	}

}
