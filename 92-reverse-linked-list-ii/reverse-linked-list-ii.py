# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: if left == right, no reversal needed
        if left == right or not head or not head.next:
            return head
        
        # Create a dummy node to handle the case when left == 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # curr is the first node to be reversed
        curr = prev.next
        
        # Reverse the sublist from left to right
        # We'll reverse by moving nodes one by one
        for _ in range(right - left):
            # Store the next node to be processed
            next_node = curr.next
            # Remove next_node from its position
            curr.next = next_node.next
            # Insert next_node right after prev
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next