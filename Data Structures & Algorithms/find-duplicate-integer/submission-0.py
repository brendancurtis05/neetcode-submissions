class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True: #there will always be a repeated number (given)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break #found where they meet
        
        slow2 = 0 #second slow pointer
        while True: #bring the second slow pointer and our intersection together
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow #this math works       


