# -*- coding: utf-8 -*-
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        for row in grid:
            row = list(row)
        width = len(grid[0])
        height = len(grid)
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    count += 1
                    self.label(grid,i,j,width,height)
        return count
    def label(self,arr,i,j,width,height):
        arr[i][j] = '*'
        if i >= 1 and arr[i-1][j] == '1':
            self.label(arr,i-1,j,width,height)
        if i <= height - 2 and arr[i+1][j] == '1':
            self.label(arr,i+1,j,width,height)
        if j >= 1 and arr[i][j-1] == '1':
            self.label(arr,i,j-1,width,height)
        if j <= width -2 and arr[i][j+1] == '1':
            self.label(arr,i,j+1,width,height)
        return
            
        

