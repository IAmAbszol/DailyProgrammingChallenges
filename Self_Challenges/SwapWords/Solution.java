/*
	This was a problem off interview.io in which
	the interviewee was tasked to write a program
	in which the arrays words were to be swapped.

	In this example, perfect makes practice
	should come out as practice makes perfect.

	Restriction(s):
		- Cannot instantiate/create a new array to hold
		changed words... too ez =]


	Devised Steps;
		1. Reverse whole string, allows for correct spots to be placed
		2. Reverse the words, this will give us our resultant string
	* Slight inspiration was off of indexOf.
	I had to really slap myself for reversing the string and NO IDEA WHY 
	I didn't realize to swap the word using some function. RIP Java method use =[

	Anyways indexOf was taken but all else is standard.

*/


import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) {

		char[] array = {'p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e'};
		solve(array);		
		System.out.println(array);

	}

	private static void solve(char[] input) {
		reverse(input, 0, input.length - 1);		
		reverseWords(input);
	}

	private static void reverse(char[] input, int start, int end) {
		while(start < end) {
			char tmp = input[start];
			input[start] = input[end];
			input[end] = tmp;
			start++;
			end--;
		}
	}

	private static void reverseWords(char[] input) {
		int current = 0;
		while(current < input.length) {
			int start = current;
			int end = indexOf(input, ' ', start);
			// Were at the end of the array
			if(end == -1) {
				end = input.length - 1;
				reverse(input, start, end);
				break;
			} else {
				reverse(input, start, end - 1);
				current = end + 1;
			}
		}
	}

	private static int indexOf(char[] input, char special, int start) {
		for(int i = start; i < input.length; i++) {
			if(input[i] == special) {
				return i;
			}
		}
		return -1;
	}	

}
