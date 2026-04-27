class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res=[]
        res.append(intervals[0])
        restrack=0
        for i in range (1,len(intervals)):
                if intervals[i][0] <= res[restrack][1]:
                    res[restrack][1]=max(intervals[i][1],res[restrack][1])
                else:
                    res.append(intervals[i])
                    restrack+=1
        return res