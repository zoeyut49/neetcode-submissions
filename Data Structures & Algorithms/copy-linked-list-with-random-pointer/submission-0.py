"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        o2n = {None: None}
        
        cur = head
        while cur:
            new = Node(cur.val)
            o2n[cur] = new
            cur = cur.next
        
        cur = head
        while cur:
            new = o2n[cur]
            new.next = o2n[cur.next]
            new.random = o2n[cur.random]
            cur = cur.next
        
        return o2n[head]