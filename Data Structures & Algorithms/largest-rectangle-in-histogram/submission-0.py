class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #while stack exists and top value of the stack is greater than the height we just reached
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) #max area is equal to height * index we started at
                start = index #set index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

