import java.io.*;
import java.util.*;

import junit.framework.*;

public class Solution {

	public static void main(String[] args) {

		int find = 28;
		int[] input = {100, 44, 60, 12, 28, 29, 13, 0, 1, 5, 33, 30, 56};
		Arrays.sort(input);
		System.out.format("Binary Search - Found value %d at index %d\n", find, binarySearch(input, 0, input.length - 1, find)); 	
		rotate(input, 3);
		System.out.format("Binary Search Rotated (3) - Found value %d at index %d\n", find, pivotBinarySearch(input, 0, input.length - 1, find)); 	

	}

	private static int pivotBinarySearch(int[] arr, int low, int high, int val) {
	// 1 2 3		1- 	3-
	// 3 1 2		3 	2-
	// 2 3 1		2- 	1-

		if(arr == null) {
			return -1;
		}

		int mid = (low + high)/2;
		if(arr[mid] == val) {
			return mid;
		}
		// We shifted it to the left
		if(arr[low] <= arr[mid]) {
			if(arr[low] <= val && val <= arr[mid]) {
				return pivotBinarySearch(arr, low, mid - 1, val);
			}
			return pivotBinarySearch(arr, mid + 1, high, val);
		}

		// Else right
		if(arr[mid] <= val && val <= arr[high]) {
			return pivotBinarySearch(arr, mid+1, high, val);
		}
		return pivotBinarySearch(arr, low, mid - 1, val);

	}

	private static int binarySearch(int[] arr, int low, int high, int val) {
		if(high < low) return -1;
		int mid = (low + high) / 2;
		if(val == arr[mid]) return mid;
		if(val > arr[mid]) return binarySearch(arr, mid + 1, high, val);
		return binarySearch(arr, low, mid - 1, val);
	}

	private static void rotate(int[] arr, int pos) {
		for(int p = 0; p < pos; p++) {
			int prev = arr[1], cur = 0;
			arr[1] = arr[0];
			for(int i = 2; i < arr.length; i++) {
				cur = arr[i];
				arr[i] = prev;
				prev = cur;
			}
			arr[0] = prev;
		}
	}

}
