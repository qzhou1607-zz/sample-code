# -*- coding: utf-8 -*-
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

@author: Qing_Zhou
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        i = 0;
        j = 0;
        spiral = [matrix[i][j]]
        while top <= bottom and left <= right:
            while j <= right - 1 and top <= bottom:
                j += 1
                spiral.append(matrix[i][j])
            top += 1
            while i <= bottom - 1 and left <= right:
                i += 1
                spiral.append(matrix[i][j])
            right -= 1
            while j >= left + 1 and top <= bottom:
                j -= 1
                spiral.append(matrix[i][j])
            bottom -= 1
            while i >= top + 1 and left <= right:
                i -= 1
                spiral.append(matrix[i][j])
            left += 1
        return spiral
            
            

