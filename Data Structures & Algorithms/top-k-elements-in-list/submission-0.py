class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap to count the occurences of each value
        freq = [[] for i in range(len(nums)+1)] #the index is the frequency/count of an elemnt. Initialize as an empty array size of input+1

        #go through every value in nums and get how many times it occurs
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #go through each value we counted
        for num, count in count.items(): #returns every key pair
            freq[count].append(num)

        res=[]
        for i in range(len(freq)-1, 0, -1):#start at last index, decrement until 0
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
            