#!user/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s.lstrip(); s.rstrip()
        s1 = "" + s[0]
        n = 1; length = len(s)
        while n < length:
            if s[n] != " ":
                s1 += s[n]
            elif s[n-1] != " ":
                s1 += s[n]
            n += 1
        length = len(s1)
        ls = [-1,]
        for i, ele in enumerate(s1):
            if ele == ' ':
                ls.append(i)
        k = ls.pop()
        if k == length - 1:
            return k - ls.pop() -1
        else:
            return length - k -1