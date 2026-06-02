import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        heapq.heapify(self.minheap)
        self.k = k
        while k < len(self.minheap):
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if self.k < len(self.minheap):
            heapq.heappop(self.minheap)
        return self.minheap[0]