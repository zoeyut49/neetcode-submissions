# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append([root, 1])
        curr_d = 1
        level = []
        res = []

        while q:
            node, d = q.popleft()
            if curr_d != d:
                res.append(level)
                level = []
                curr_d = d
            level.append(node.val)
            if node.left: q.append([node.left, d+1])
            if node.right: q.append([node.right, d+1])

        res.append(level)

        return res