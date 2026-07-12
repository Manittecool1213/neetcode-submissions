"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import math
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start, reverse = True)

        rooms = [intervals[-1].end]
        intervals.pop()
        while intervals:
            start, end = intervals[-1].start, intervals[-1].end
            intervals.pop()

            min_diff = math.inf
            min_diff_index = -1
            for i in range(len(rooms)):
                if start >= rooms[i]:
                    min_diff = min(start - rooms[i], min_diff)
                    min_diff_index = i
            
            if min_diff < math.inf:
                rooms[min_diff_index] = end
            else:
                rooms.append(end)

        return len(rooms)
