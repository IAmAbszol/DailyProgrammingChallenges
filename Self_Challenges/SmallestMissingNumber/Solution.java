import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) {

		int[] input = {0,5,3,1,4};
		System.out.println(smallestMissingNumber(input));

	}

	private static int smallestMissingNumber(int[] input) {

		if(input == null) {
			return -1;
		}

		// What about if it's unsorted?
		ArrayList<Integer> intSort = new ArrayList<Integer>();
		for(int i : input) {
			intSort.add(i);
		}
		Collections.sort(intSort);
		input = new int[intSort.size()];
		Iterator<Integer> iter = intSort.iterator();
		for(int i = 0; i < intSort.size(); i++) {
			input[i] = iter.next().intValue();
		}

		for(int i = 0; i < input.length; i++) {

			if(input[i] != i) {
				return i;
			}

		}
		return input.length;

	}

}
