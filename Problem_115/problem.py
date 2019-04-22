'''

            S               T
            12              6
        6       16      3       5
    3       5              4
       4               

    1. Start at root of S
    2. Add root to queue
    3. Loop 
        a. Check if root equals T's root
            Yes - Go to helper function
        b. Add left and right to queue if exists

    Helper
        1. If root left and root right == S's node left and right, continue.
        2. If not, return False
        3. If both are none, return True

'''

from queue import Queue

class Node:

        def __init__(self, value, left=None, right=None):
            self.value = value 
            self.left = left
            self.right = right

def problem(s_root, t_root):
    if s_root is None:
        return None

    def helper(node, t_root):
        if node is None and t_root is None:
            return True
        if node is None and t_root is not None:
            return False
        if node is not None and t_root is None:
            return False
        if node.value != t_root.value:
            return False
        ret_left = helper(node.left, t_root.left)
        ret_right = helper(node.right, t_root.right)
        return ret_left and ret_right

    q = Queue()
    q.put(s_root)
    while not q.empty():
        node = q.get()
        if node.value == t_root.value and helper(node, t_root):
            return True
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return False

s = Node(12, left=Node(6, left=Node(3, right=Node(4)), right=Node(5)), right=Node(16))
t = Node(6, left=Node(3, right=Node(4)), right=Node(5))

print(problem(s, t))