from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        If we traverse the tree using a BFS we will have access to each
        level of the binary tree, which then makes a horizontal (right) association
        easier.
        """
        if not root:
            return root

        queue = deque()

        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                currNode = queue.popleft()
                if i < size - 1:
                    currNode.next = queue[0]
                # add children
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

        return root
            
