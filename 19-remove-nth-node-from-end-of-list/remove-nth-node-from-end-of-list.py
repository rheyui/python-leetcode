# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):

        # Count total nodes
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        # If first node must be removed
        if count == n:
            return head.next

        # Find node before target
        temp = head

        for i in range(count - n - 1):
            temp = temp.next

        # Remove node
        temp.next = temp.next.next

        return head