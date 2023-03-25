"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

#NOT WORKING PROPERLY

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Looping condition:
        if root == None:
            return
        node = root
        
        # Needs two pointers:
            # One for parent node
            # One for eldest child node
            
        # For progressing to next level
        while node != None:
            node.left.next = node.right
            
            # For each level
            while node != None:
                print(node.val, node.left, node.right, node.next)
                #First type of connection, for sibling node
                node.left.next = node.right

                #Second type of connection, if there is a cousin node
                if node.next:
                    node.right.next = node.next.left
                  
                # Move to next parent
                node = node.next
                
        return root
        
        