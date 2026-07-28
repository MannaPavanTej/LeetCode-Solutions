# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr is not None:
            l += 1
            curr = curr.next
        
        # Edge Case: If we need to remove the head node
        if l == n:
            return head.next
            
        # Pass 2: Reset curr and stop right BEFORE the node to delete
        curr = head
        for i in range(l - n - 1):
            curr = curr.next
            
        # Skip the target node
        curr.next = curr.next.next
        
        return head