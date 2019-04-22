'''
    The past two I haven't coded as I've either done them or just wanted to give
    a general oversight of it.

    This problem though I haven't encountered but it's a nifty one.

    [-9, -2, 0, 2, 3]
    We can actually sort this list given any sorting algorithm as the problem wants the square of each number
    as it's final result but sorted. Negatives don't appear in squares so were safe to assume these
    can be all treated like positive integers.
    
    For this, I could choose Insertion Sort (O(n^2) time)
    or
    Merge sort (Same complexity but not as often)

    I'll use Insertion Sort
'''

def problem(arr):
    if arr is None:
        return None
    arr = [a ** 2 for a in arr]
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr

    
