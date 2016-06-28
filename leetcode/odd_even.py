#!user/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head; q = head.next
        while p and q:
            fg = q.next
            if fg:
                q.next = fg.next
                fg.next = p.next
                p.next = fg
                p = p.next
                q = q.next
        return head

if __name__ == '__main__':
    inlist = [1, 2, 3, 4, 5, 6, 7, 8]
    head = ListNode(None)
    ls = head
    for i in inlist:
        head.next = head = ListNode(i)
    head = Solution().oddEvenList(ls.next)
    print ls.next
