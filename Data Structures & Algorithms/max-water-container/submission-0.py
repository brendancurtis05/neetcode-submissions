class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_Area = 0
        l=0
        r=n-1

        while l<r:
            w = r-l
            h = min(heights[r], heights[l])
            area = w*h

            max_Area = max(area, max_Area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_Area     
        