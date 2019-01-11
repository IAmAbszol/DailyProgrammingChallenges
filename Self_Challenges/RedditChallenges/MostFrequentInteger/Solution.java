import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) {

		int[] arr = {0,1,2,3,4,4,2,5,4};
		System.out.println("Most Frequent Integer is " + solve(arr));

	}

	private static int solve(int[] arr) {

		if(arr == null) {
			return -1;
		} else if(arr.length == 1) {
			return arr[0];
		}

		int frequentInt = 0;
		int count = 0;
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		for(int i = 0; i < arr.length; i++) {
			// Initial condition
			if(frequentInt == 0) {
				frequentInt = arr[i];
				count = 1;
				map.put(frequentInt, count);
				continue;
			}
			// New key has arrived
			if(!map.containsKey(arr[i])) {
				map.put(arr[i], 1);
				continue;
			}
			// Update existing, perform analysis
			int val = map.get(arr[i]);
			val++;
			// Newest most frequent found
			if(val > count) {
				frequentInt = arr[i];
				count = val;
			}
			map.put(arr[i], val);
		}
		return frequentInt;
	}
	
}
