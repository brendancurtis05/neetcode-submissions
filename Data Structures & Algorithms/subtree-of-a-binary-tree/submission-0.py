# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot: return True #ORDER IS IMPORTANT
        if not root: return False #could write "and subRoot"

        if self.sameTree(subRoot, root):
            return True

        #recursive call subtree function
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))



    def sameTree(self, s, t):
        if not s and not t: #both null
            return True
        
        if s and t and s.val == t.val: #if node is equal
        #recursive search
            return (self.sameTree(s.right, t.right) and 
                    self.sameTree(s.left, t.left))
        else:
            return False
