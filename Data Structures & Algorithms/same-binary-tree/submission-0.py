# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stk = [[p, q]]

        while stk:
            node = stk.pop()
            if not node[0] and not node[1]:
                continue
            if not node[0] or not node[1]:
                return False
            if node[0].val != node[1].val:
                return False
            stk.append([node[0].right, node[1].right])
            stk.append([node[0].left, node[1].left])

        return True