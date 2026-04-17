class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minhp= []
        for x,y in points:
            temp = x*x + y*y
            heapq.heappush(minhp,(temp,[x,y]))
        res=[]
        for _ in range (k):
            res.append(heapq.heappop(minhp)[1])
        return res