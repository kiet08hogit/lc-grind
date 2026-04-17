class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minhp=[]
        dist,arr=0,[]
        res=[]
        for first, second in points:
            temp = (first**2)+(second**2)
            heapq.heappush(minhp, (temp,(first,second)))
        for i in range (k):
            dist,arr= heapq.heappop(minhp)
            res.append(arr)
        return res