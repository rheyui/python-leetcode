# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):

        # Base case
        if not head or not head.next:
            return head

        first = head
        second = head.next

        # Swap remaining list
        first.next = self.swapPairs(second.next)
        second.next = first

        return second