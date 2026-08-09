# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #calculate the max path at each node recursively since each path has to split at any given node

        #global variable
        res = [root.val]

        def dfs(root):
            #base case
            if not root:
                return 0

            #find max path of each subtree
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            #could be negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            #return max path without spliting 
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

        #could return max path sum with split and max path sum WITHOUT split in order to not use res global variable



