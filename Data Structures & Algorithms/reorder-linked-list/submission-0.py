# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodel = []
        cur = head
        while cur:
            nodel.append(cur)
            cur = cur.next
        
        l, r = 0, len(nodel) - 1
        while l < r:
            nodel[l].next = nodel[r]
            l += 1
            if l >= r:
                break
            nodel[r].next = nodel[l]
            r -= 1
        
        nodel[r].next = None
