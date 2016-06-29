#! user/bin/env python
# -*- coding:utf-8 -*-
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            result.append(root.val)
            p = root.right; q = root
            flag = True
            while p or flag:
                if p:
                    result.append(p.val)
                    flag = False
                elif not p and q.left:
                    p = q.left
                    result.append(p.val)
                    flag = True
                else:
                    flag = False
                p = p.right
        return result
