# -*- coding: utf-8 -*-
"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

@author: Qing_Zhou
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []
        nodes = []
        while len(nodes) > 0 or root != None:
            if root != None:
                preorder.append(root.val)
                nodes.append(root)
                root = root.left
            if root == None:
                root = nodes.pop()
                root = root.right
        return preorder
        