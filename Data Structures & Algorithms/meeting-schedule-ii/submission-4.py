"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s= e=0
        rooms =0
        maxrooms=0
        # s= [1,5,10,15]
        # e= [5,10,15,20]
        while s < len(intervals):
            if  starts[s] < ends[e]:
                rooms +=1
                s+=1
            else:
                rooms-=1
                e+=1
            maxrooms= max(rooms,maxrooms)
        return maxrooms