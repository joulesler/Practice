# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middleNode = head
        nxt = head
        alternate = True
        while nxt.next != None:
            if alternate:
                middleNode = middleNode.next
                alternate = False
            else:
                alternate = True
            nxt = nxt.next
        return middleNode