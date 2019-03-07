import java.util.*;
import java.io.*;

public class Problem {

	public int[] closestToZero(int[] arr) {
		if (arr == null) {
			return null;
		}
		int start = 0;
		int end = arr.length - 1;
		int diffToZero = 1000;
		int x = 0;
		int y = 0;
		while (start < end) {
			int summed = arr[start] + arr[end];
			if (Math.abs(summed) < diffToZero) {
				diffToZero = Math.abs(summed);
				x = arr[start];
				y = arr[end];
			}
			if (summed < 0) {
				start += 1;
			} else {
				end -= 1;
			}
		}
		return new int[] { x, y};
	}

	/*
	public int[] closestToZero(int[] arr) {
		if (arr == null) {
			return null;
		}
		Arrays.sort(arr);
		int start = 0;
		int end = arr.length - 1;
		int diffToZero = 1000;
		int x = 0;
		int y = 0;
		while (start < end) {
			if (Math.abs(arr[start] + arr[end]) < diffToZero) {
				x = arr[start];
				y = arr[end];
				diffToZero = Math.abs(arr[start] + arr[end]);
			}
			start += 1;
			end -= 1;
		}
		return new int[] { x, y };
	}
	*/

	public static void main(String[] args) {
		int[] arr = {-1, 10, 5, -9, -8};
		Problem prob = new Problem();
		int[] result = prob.closestToZero(arr);
		System.out.println(result[0] + ", " + result[1]);
	}

}
