#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
        :type obstacleGrid: List[List[int]]
        :rtype: int
        '''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break

        for j in range(m):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]          

        
                            

if __name__ == '__main__':
    a = [[0]] # Expected 1
    print Solution().uniquePathsWithObstacles(a)

    b = [[0,0,0],[0,1,0],[0,0,0]]  # Expected 2
    print Solution().uniquePathsWithObstacles(b)

    c = [[0,0],[1,1],[0,0]] # Expected 0
    print Solution().uniquePathsWithObstacles(c)

# Dynamic Programing Problem
# dp[i][j] = d[i-1][j] + d[i][j-1]
