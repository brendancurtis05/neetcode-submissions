class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] #arbitrary value
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]: #already sorted array
                res = min(res, nums[l])
                break

            m = (l+r)//2
            res = min(res, nums[m]) #update min just incase
            if nums[m] >= nums[l]: #part of left sorted portion of nums
                l = m+1
            else:
                r = m-1
            
        return res