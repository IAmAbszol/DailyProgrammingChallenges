import java.util.*;
import java.io.*;

public class Solution {
	
	public static void main(String[] args) {

		char[] input = {'1','5','4','3','6','2'};
		// solution
		pancakeSort(input);
		System.out.println(input);	

	}

	private static void pancakeSort(char[] input) {

		if(input == null || input.length < 2) {
			return;
		}
		for(int i = input.length - 1; i >= 0; i--) {
			int maxElement = i;
			for(int j = i; j >= 0; j--) {
				if(input[j] > input[maxElement]) {
					maxElement = j;
				}
			}
			flip(input, maxElement + 1);
			flip(input, i + 1);
		}
	
	}

	private static void flip(char[] input, int k) {

		if(input == null || input.length < 2) {
			return;
		}

		for(int i = 0; i < k/2; i++) {
			char tmp = input[i];
			input[i] = input[k - i - 1];
			input[k - i - 1] = tmp;
		}

	}

}
