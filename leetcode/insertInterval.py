#! user/bin/env python
# -*- encoding:utf-8 -*-

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def inInterval(self, n):
        if n >= self.start and n <= self.end:
            return True
        return False

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # solution one
        # length = len(intervals)
        # for i, ele in enumerate(intervals):
        #     if (newInterval.start >= ele.start and newInterval.start <= ele.end) or \
        #             (newInterval.end >= ele.start and newInterval.end <= ele.end) or \
        #             (ele.start >= newInterval.start and ele.start <= newInterval.end) or \
        #             (ele.end >= newInterval.start and ele.end <= newInterval.end):
        #         tempInterval = intervals.pop(i)
        #         tempList = [newInterval.start, newInterval.end, tempInterval.end, tempInterval.start]
        #         tempList.sort()
        #         newInterval.start = tempList[0]
        #         newInterval.end = tempList[-1]
        #         self.insert(intervals, newInterval)
        # flag = False
        # for ele in intervals:
        #     if ele.start == newInterval.start and ele.end == newInterval.end:
        #         flag = True
        # if not flag:
        #     intervals.append(newInterval)
        #     intervals = sorted(intervals, key = lambda x:x.start)
        # return intervals
        # ----------------------------------------------------------

        # solution two
        # s, e = newInterval.start, newInterval.end
        # left = [i for i in intervals if i.end < s]
        # right = [i for i in intervals if i.start > e]
        # if left + right != intervals:
        #     s = min(s, intervals[len(left)].start)
        #     e = max(e, intervals[~len(right)].end)
        # return left + [Interval(s, e)] + right
        # ----------------------------------------------------------

        # solution three
        # s, e = newInterval.start, newInterval.end
        # parts = merge, left, right = [], [], []
        # for i in intervals:
        #     parts[(i.end < s) - (i.start > e)].append(i)
        # if merge:
        #     s = min(s, merge[0].start)
        #     e = max(e, merge[-1].end)
        # return left + [Interval(s, e)] + right
        # ----------------------------------------------------------

        # solution four
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right

if __name__ == "__main__":
    newInterval = Interval(2, 3)
    intervals = []
    intervals.append(Interval(1, 5))
    Solution().insert(intervals, newInterval)
