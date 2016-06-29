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
        # this is DFS-tree solution( using recursive )
        # def collect(node, depth):
        #     if node:
        #         if depth == len(view):
        #             view.append(node.val)
        #         collect(node.right, depth + 1)
        #         collect(node.left, depth + 1)
        #
        # view = []
        # collect(root, 0)
        # return view

        valList = []; nodeList = []
        if not root:
            return valList
        nodeList.append(root)
        while nodeList:
            tmpList = nodeList
            for i in range(len(tmpList)):
                ele = nodeList.pop(0)
                if ele.left:
                    nodeList.append(ele.left)
                if ele.right:
                    nodeList.append(ele.right)
            valList.append(ele.val)
        return valList

