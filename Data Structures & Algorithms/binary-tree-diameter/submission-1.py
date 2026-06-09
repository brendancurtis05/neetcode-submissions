# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #result variable
        res = 0

        #iterative dfs func
        def dfs(root):

            nonlocal res #need a nonlocal res

            if not root: #base case
                return 0

            #iterate left and right 
            left = dfs(root.left)
            right = dfs(root.right)

            #result is our highest found diameter so far
            res = max(res, left+right)
            #return 1 + max of left or right
            return 1 + max(left, right)

        dfs(root)
        return res
        
        