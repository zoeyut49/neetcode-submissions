# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newl = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                newl.next = list1
                list1 = list1.next
            else:
                newl.next = list2
                list2 = list2.next
            newl = newl.next
        
        if list1 is None:
            newl.next = list2
        elif list2 is None:
            newl.next = list1
        
        return dummy.next