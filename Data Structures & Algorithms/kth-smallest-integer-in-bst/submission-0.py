# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 #num of elements we've visisted from our tree
        stack = [] #solving this iteratively
        cur = root

        while cur or stack: #go left as far as we can
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()#when the loop ends, cur is at null so we have to pop the most recently added value
            n += 1
            if n == k: #guarenteed k nodes in our tree
                return cur.val
            cur = cur.right
