# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stk = [[root, 1]]
        res = 1

        while stk:
            node,d = stk.pop()
            res = max(res,d)
            if node.right: 
                stk.append([node.right, d+1])
            if node.left: 
                stk.append([node.left, d+1])
            
        return res