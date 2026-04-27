class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res=[]
        res.append(intervals[0])
        for i in range (1,len(intervals)):
                if intervals[i][0] <= res[-1][1]:
                    res[-1][1]=max(intervals[i][1],res[-1][1])
                else:
                    res.append(intervals[i])
        print(res)
        return res