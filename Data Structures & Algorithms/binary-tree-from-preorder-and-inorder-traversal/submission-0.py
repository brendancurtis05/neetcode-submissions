# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder or not inorder:
            return None
        
        #create tree node
        root = TreeNode(preorder[0])#first element in prorder array will always be the root of the tree
        mid = inorder.index(preorder[0])#locate where the root is in the inorder array
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root