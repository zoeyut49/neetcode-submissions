import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            d = math.sqrt(points[i][0]**2 + points[i][1]**2)
            minHeap.append((d, i))
        
        heapq.heapify(minHeap)

        res = []
        for j in range(k):
            minPoint = heapq.heappop(minHeap)
            res.append(points[minPoint[1]])
        
        return res