# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #result
        q = collections.deque([root]) #making a queue, starting with our root node

        while q:
            rightSide = None
            qLen = len(q)
            
            for i in range(qLen): #go through every element at this level
                node = q.popleft()
                if node:
                    rightSide = node #rightside will contain the last node that was at the current level of the que
                    q.append(node.left)
                    q.append(node.right)

            if rightSide: #could eb null
                res.append(rightSide.val)
        return res
        