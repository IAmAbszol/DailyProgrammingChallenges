import java.util.*;
import java.io.*;

public class MaximumSubarray {

	public int kadanes(int[] arr) {
		int maxCurrent = 0, maxEnding = 0;
		for (int i = 0; i < arr.length; i++) {
			maxEnding = Math.max(arr[i], maxEnding + arr[i]);
			maxCurrent = Math.max(maxCurrent, maxEnding);
		}
		return maxCurrent;
	}

	public static void main(String[] args) {
		int[] arr = { 34, -50, 42, 14, -5, 86 };
		MaximumSubarray maxSub = new MaximumSubarray();
		System.out.println(maxSub.kadanes(arr));
	}

}
