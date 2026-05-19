# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle point of the list
        slow, fast = head, head.next

        while fast and fast.next:#while not null
            slow = slow.next
            fast = fast.next.next

        second = slow.next #second half of the list
        prev = slow.next = None

        while second: #reversing the second portion of the linked list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge two halves
        first, second = head, prev
        while second: #the second half of the list will always be <= the first half
                      #because of how we are handling even/odd lists
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2