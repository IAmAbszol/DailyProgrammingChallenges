package daily;

import java.util.Stack;

public class DailyProblem17 {

	private static int count(Stack s) {
		int k = 0;
		while(!s.isEmpty()) {
			String strip = ((String)s.pop()).replaceAll("/t", "");
			k += strip.length();
		}
		return k;
	}
	
	public static void main(String[] args) {
	
		int longest = 0;
		Stack best = null;
		
		String path = "dir/n/tsubdir1/n/t/tfile1.ext/n/t/tsubsubdir1/n/tsubdir2/n/t/tsubsubdir2/n/t/t/tfile2.ext";
		String[] files = path.split("/n");
		
		Stack pathStack = new Stack();
		for(String file : files) {
			// Add root 'dir' to stack.
			if(pathStack.isEmpty()) {
				pathStack.push(file);
				continue;
			}
			String peeked = (String) pathStack.peek();
			
			// Same part of the directory.
			if(peeked.split("/t").length == file.split("/t").length) {
				pathStack.pop();
				pathStack.push(file);
				
			// We're continuing our descent.
			} else if(peeked.split("/t").length < file.split("/t").length) {
				
				pathStack.push(file);
				
			// We're back up, remove all files not within group.
			} else {
				while (((String)pathStack.peek()).split("/t").length != file.split("/t").length) {
					pathStack.pop();
				}
				pathStack.pop();
				pathStack.push(file);
			}
			
			// Check if file, if so, then find out its length.
			if(file.contains(".")) {
				int found = count((Stack<String>)pathStack.clone());
				if(found > longest) {
					longest = found;
					best = (Stack<String>)pathStack.clone();
				}
			}
			
		}
		
		System.out.println("Longest : " + longest);
		String list = "";
		while(!best.isEmpty()) {
			list = ((String)best.pop()).replaceAll("/t", "") + "/" + list;
		}
		System.out.println(list);
	
	}

}