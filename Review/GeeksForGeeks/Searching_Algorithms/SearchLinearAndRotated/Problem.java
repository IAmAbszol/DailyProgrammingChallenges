import java.util.*;
import java.io.*;

public class Problem {

	public int search(int[] arr, int val) {

		Arrays.sort(arr);
		int low = 0;
		int high = arr.length - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (arr[mid] == val) {
				return mid;
			}
			if (arr[mid] > val) {
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		return -1;
	}


	public int rotated_search(int[] arr, int val) {
		int low = 0;
		int high = arr.length - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (arr[mid] == val) {
				return mid;
			}
			if (arr[low] <= arr[mid]) {
				if (val >= arr[low] && val <= arr[mid]) {
					high = mid - 1;
				} else {
					low = mid + 1;
				}
			} else {
				if (val >= arr[mid] && val <= arr[high]) {
					low = mid + 1;
				} else {
					high = mid - 1;
				}
			}
		}
		return -1;
	}

	public static void main(String[] args) {

		int[] arr = new int[] { 0, 9, 3, 100, 6, 53, 2, 95, 20 };

		Problem prob = new Problem();
		System.out.println(prob.search(arr, 6));
		System.out.println(prob.search(arr, 5));

		arr = new int[] { 3, 4, 5, 1, 2 };
		System.out.println(prob.rotated_search(arr, 1));
		System.out.println(prob.rotated_search(arr, 3));
	}

}
