#!user/bin/env python
# -*- coding:utf-8 -*-

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1; end = n
        mid = (start + end) / 2
        flag = mid
        while start <= end:
            mid = (start + end) / 2
            if isBadVersion(mid):
                flag = mid
                end = mid - 1
            else:
                start = mid + 1
        return flag

