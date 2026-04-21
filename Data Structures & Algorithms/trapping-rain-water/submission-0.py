class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: #if the list is empty
            return 0

        l, r = 0, len(height)-1 #left and right pointer
        leftMax, rightMax = height[l], height[r] #max height of left and right pointer
        res = 0 #result

        while l < r:
            if leftMax < rightMax: #take the minimum max height
                l += 1 #increase pointer
                leftMax = max(leftMax, height[l]) #find new max
                res += leftMax - height[l] #append max - current height (always be >=0)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
            
