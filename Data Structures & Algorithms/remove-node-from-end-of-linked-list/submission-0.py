# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        #2 pointers always being n away so left will help us find the one to remove because we will 
        #have l be right before the one we want to remove
        left = dummy
        right = head 

        #loop to get left and right n distance away
        while n > 0 and right: 
            right = right.next
            n -= 1
        #keep moving till right hits end of list
        while right:
            left = left.next
            right = right.next
        
        #delete node
        left.next = left.next.next
        return dummy.next


                