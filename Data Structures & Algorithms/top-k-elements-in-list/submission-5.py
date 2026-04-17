import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heapmap={}
        maxheap=[]
        result=[]
        for num in nums:
            if num in heapmap:
                heapmap[num]+=1
            else:
                heapmap[num]=1

        for key, value in heapmap.items():
            heapq.heappush(maxheap,(-value,key))
        for i in range(k):
            if maxheap:
                value, key=heapq.heappop(maxheap)
                result.append(key)
        return result

   
        
    