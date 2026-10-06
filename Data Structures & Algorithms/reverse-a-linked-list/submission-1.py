# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


        #pretty intuitive
        #Time: O(n), Space: O(1)

        #RECURSIVE:
        """
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head #reverse the link from next node and head
        head.next = None #if head is the first node in the list
        return newHead
        """

        