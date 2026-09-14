"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals by start time (first element of each interval)
        intervals.sort(key=lambda x: x.start)
        for i in range(1,len(intervals)):
            if intervals[i].start<intervals[i-1].end:
                return False
        return True
    #Time and space complexity is O(n*logn ) and O(n) respectively