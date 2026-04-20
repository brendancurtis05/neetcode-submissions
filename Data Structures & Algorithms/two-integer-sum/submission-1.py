class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target = 7
        #nums = [3,4,5,6]

        prevMap = {}

        for i, n in enumerate(nums): #loop
            diff = target-n #1.7-3 = 4          #2.7-4 = 3
            if diff in prevMap: #1.4 not in prevMap     #2.3 in previous map
                return [prevMap[diff], i] #found a match, return [0,1]
            prevMap[n]=i #prevMap[3] = 0