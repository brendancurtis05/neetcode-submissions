class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n) time
        #output does not count at extra memory for this problem so O(1) space

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
