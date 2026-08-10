class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #max heap solution
        #nlog(n)
        #python does not have max heaps, only min heaps, so we need to multiply every value by -1
        
        stones = [-s for s in stones]
        heapq.heapify(stones) #O(n)

        while len(stones) > 1:
            first = heapq.heappop(stones) #heaviest stone
            second = heapq.heappop(stones) #second heaviest stone
            if second > first: #working with negatives
                heapq.heappush(stones, first-second)
            else:
                heapq.heappush(stones, second-first)
        
        return -1 * heapq.heappop(stones)