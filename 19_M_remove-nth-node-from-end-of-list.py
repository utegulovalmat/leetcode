# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
                3    
        0 1 2 3 4 5 6
                  * 
                    *
        
        """
        if not head:
            return head
        
        dh = ListNode()
        dh.next = head
        slow = dh
        fast = dh
        
        while n+1:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dh.next
        