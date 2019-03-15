import java.util.*;
import java.io.*;

public class SmallestWindow {

	public int[] solve(int[] arr) {
		if (arr == null || arr.length < 2) {
			return arr;
		}
		/*
			start = end = 0
			3 7 5 6 9
			3 
			end += 1
			3 7 start += 1
			3 5 7 end += 1
			3 5 6 7 end += 1
		*/
		int maxValue = Integer.MAX_VALUE, minValue = Integer.MIN_VALUE;
		int left = 0, right = 0;
		for (int i = 0; i < arr.length; i++) {
			maxValue = Math.max(maxValue, arr[i]);
			if (arr[i] < maxValue) {
				right = i;
			}
		}
		for (int i = arr.length - 1; i > 0; i--) {
			minValue = Math.min(minValue, arr[i]);
			if (arr[i] > minValue) {
				left = i;
			}
		}
		return new int[] { left, right };
	}

	public static void main(String[] args) {
		int[] arr = { 3, 7, 5, 6, 9 };
		
		SmallestWindow window = new SmallestWindow();
		int[] position = window.solve(arr);
		System.out.println(position[0]  + ", " + position[1]);
	}

}
