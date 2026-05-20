# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointers approach, make sure gap between pointers = n+1
        dummy = ListNode(0, head)
        left = dummy
        #right = head + n
        right = head
        while n > 0 and right: #loop to shift correctly
            right = right.next
            n-=1
        
        #when right is at the end of the list, the left will be 1 node before the node to delete
        while right:
            left = left.next
            right = right.next

        #delete node
        left.next = left.next.next
        
        return dummy.next

        