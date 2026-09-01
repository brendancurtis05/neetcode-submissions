class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.minHeap, self.k = nums, k #initialize k and min heap
        heapq.heapify(self.minHeap) #heapify
        while len(self.minHeap) > k: #we are keeping min heap to have only k nodes
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #push whatever value onto heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #pop smallest
        return self.minHeap[0]
        
