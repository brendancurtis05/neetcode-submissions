class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [] #create our maxheap
        for x, y in points: #for each point
            dist = -(x**2 + y**2) #compute the negative distance
            heapq.heappush(maxHeap, [dist, x, y]) #push negative distance
            if (len(maxHeap) > k): #if we have too many points
                heapq.heappop(maxHeap) #pop farthest one (smallest number since we are computing negative)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
        