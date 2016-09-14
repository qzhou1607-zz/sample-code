# -*- coding: utf-8 -*-
"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

@author: Qing_Zhou
"""

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
        if root == None:
            return []
        all_levels = []
        current = [root]
        while len(current) > 0:
            level = []
            next = []
            for i in range(len(current)):
                p = current[i]
                level.append(p.val)
                if p.left != None:
                    next.append(p.left)
                if p.right != None:
                    next.append(p.right)
            all_levels.append(level[-1])
            current = next
        return all_levels