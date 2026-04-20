class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] #need to return a list of lists
        nums.sort() #sort the array O(nlogn)

        for i, a in enumerate(nums): #practically going through nums and performing Two Sum II on each index
            if i>0 and a == nums[i-1]: #if index is greater than 0 and the value at the index is the same as the previous, we can skip
                continue
            l,r = i+1, len(nums)-1 #set left and right pointers
            while l<r: 
                threeSum = a + nums[l] + nums[r] #perform two sum II

                if threeSum > 0: #target will always be 0
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) #append the result list
                    l += 1 #move left pointer over to search for more results
                    while nums[l] == nums[l-1] and l<r: #while value at left is the same as the next value, keep indexing left pointer
                        l+=1
        return res
                