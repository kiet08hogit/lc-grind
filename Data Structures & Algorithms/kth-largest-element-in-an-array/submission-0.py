class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap= [-x for x in nums]
        heapq.heapify(max_heap)
        for i in range (k-1):
            if max_heap:
                heapq.heappop(max_heap) 
        result= -heapq.heappop(max_heap) 
        return result