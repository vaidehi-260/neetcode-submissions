# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        curr = temp = head
        while curr:
            a.append(curr)
            curr = curr.next
        node =len(a)-n
        if node == 0:
            return head.next
        
        a[len(a)-n-1].next = a[len(a)-n].next
        return head

        