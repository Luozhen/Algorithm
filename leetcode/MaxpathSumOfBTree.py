#!user/bin/env python
# -*- coding:utf-8 -*-

# Given a binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def deepPathSum(root):
            if not root:
                return 0
            leftDeep = deepPathSum(root.left)
            rightDeep = deepPathSum(root.right)
            node = (root, leftDeep, rightDeep)
            listNode.append(node)
            return root.val + max(leftDeep, rightDeep)
        listNode = []
        head = TreeNode(0); head.left = root
        deepPathSum(head)
        maxDp = 0
        for ele in iter(listNode):
            sumDp = sum(x for x in ele)
            if sumDp >= maxDp:
                maxDp = sumDp
        return maxDp

