import java.util.Arrays;

public class Problem {

	public static void main(String[] args) {

		String[] array = {"dog", "deer", "deal", "dingo", "diaper", "arvark"};
		String developing = args[0];

		Arrays.sort(array);
	
		for(int i = 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
	
		for(int i = 0; i < array.length; i++) {
			System.out.println(developing + " -> " + array[i] + " : " + developing.compareTo(array[i]));
		}
	
//		System.out.println(binary_search(array, developing));
		
	}
/*
	private static String[] binary_search(String[] dict, String word) {

		int low = 0;
		int mid = 0;
		int high = dict.length - 1;

		while (low <= high) {
			
			mid = (low + high) / 2;
		
			if (dict[mid].compareTo(word) < 0) {
				low = mid + 1;
			} else if (dict[mid].comareTo(word) > 0) {
				high = mid - 1;
			} else {
				return dict[mid];
			}

		}

		System.out.println(low + " " + mid + " " + high);

	}
*/
}
