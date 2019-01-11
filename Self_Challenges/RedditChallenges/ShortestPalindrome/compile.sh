echo -n "Compiling Solution.java... "
if javac -cp ../junit-4.13-beta-1.jar:. Solution.java ; then
	echo "Completed."
	java Solution
else
	echo "Failed."
fi

