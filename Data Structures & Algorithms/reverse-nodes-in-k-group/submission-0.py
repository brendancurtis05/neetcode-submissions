# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #code to reverse a node
        dummy = ListNode(0,head)
        groupPrev = dummy #we need to have a pointer right before the start of our curr group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: #end of list
                break
            groupNext = kth.next #one node right after our group

            #reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            #MOST COMPLICATED PART
            temp = groupPrev.next #first node in our group
            groupPrev.next = kth #now putting kth as the begining of our loop
            groupPrev = temp
            
        return dummy.next


    def getKth(self, curr, k): #helper function
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr