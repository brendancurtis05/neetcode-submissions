# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs using a queue O(n)
        res = []
        q = collections.deque()
        q.append(root)

        while q: #while queue is not empty
            qLen = len(q)
            level = [] #seperate list for every level
            for i in range(qLen): #loop through every value in our current queue
                node = q.popleft() #fifo
                if node: #if node exists
                    level.append(node.val) #append val to level list
                    q.append(node.left) #add children to queue
                    q.append(node.right)
            if level: #make sure level isnt null
                res.append(level)
        return res


        