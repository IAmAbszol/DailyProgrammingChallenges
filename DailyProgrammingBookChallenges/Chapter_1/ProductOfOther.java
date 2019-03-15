import java.util.*;
import java.io.*;

public class ProductOfOther {

	public int[] product(int[] arr) {
		if (arr == null || arr.length == 0) {
			return arr;
		}
		/*
			3 2 1
			0 3 3
			2 3 6
			2 3 6
			
			1. Create a separate array of products
			2. Iterate through the default array
				1. Add n to array of products if i == 0, else n * i
				2. Don't add n to i if i == idx of n
			3. Result 	
			Optimal solution, compute prefix and suffix, middle is the relation of p and s.
		*/
		int[] products = new int[arr.length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr.length; j++) {
				if (i == j) {
					continue;
				}
				if (products[j] == 0) {
					products[j] = arr[i];
					continue;
				}
				products[j] *= arr[i];
			}
		}
		return products;
	}

	public static void main(String[] args) {
		int[] arr = { 3, 2, 1 };
		
		ProductOfOther prod = new ProductOfOther();
		arr = prod.product(arr);
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

}
