class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        res=[]
        res.append(intervals[0])
        for i in range (1, len(intervals)):
            if intervals[i][0] < res[-1][1]:
                continue
            else:
                res.append(intervals[i])
        return len(intervals) - len(res)