# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        cur = root
        while cur: #always a result in this problem
            if p.val > cur.val and q.val > cur.val: #if both values are greater
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: #if both values are less
                cur = cur.left
            else: #one value is left and the other is right (this is the least common ancestor)
                return cur


        