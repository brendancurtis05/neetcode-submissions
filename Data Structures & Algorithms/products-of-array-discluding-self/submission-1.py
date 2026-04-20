class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n) time
        #output does not count at extra memory for this problem so O(1) space

        res = [1] * (len(nums))

        prefix = 1 #this is kind of like the prefix array from the video
        for i in range(len(nums)): # itterate through the nums array
            res[i] = prefix #result array at index i = prefix value
            prefix *= nums[i] #our prefix value is then multiplied by the number at i in nums
        postfix = 1 #same as prefix but backwards
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
