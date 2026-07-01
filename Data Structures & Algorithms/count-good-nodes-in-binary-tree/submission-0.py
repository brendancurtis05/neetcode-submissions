# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #preorder traversal
        #root node will always be a good node
        #run dfs on left and right and also pass the greatest value we've seen so far

        def dfs(node, highestVal):
            if not node: #base case
                return 0
            res = 1 if node.val >= highestVal else 0 #if its a good val
            highestVal = max(highestVal, node.val) #update highest val
            res += dfs(node.left, highestVal) #dfs recurse down the tree
            res += dfs(node.right, highestVal)
            return res
        return dfs(root, root.val)
            