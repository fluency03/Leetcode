#!/usr/bin/python
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
# vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:
# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution:
	# @param grid, a list of list of characters
	# @return an integer
	def numIslands(self, grid):
		# print (grid)
		result = 0
		if not len(grid):
			return result
		m, n = len(grid), len(grid[0])
		visited = [ [False]*n for x in range(m) ]
		for x in range(m):
			for y in range(n):
				if grid[x][y]=='1' and not visited[x][y]:
					result += 1
					self.BFS(grid, visited, x, y, m, n)
		return result
	def BFS(self, grid, visited, x, y, m, n):
		direction = zip( [1, 0, -1, 0], [0, 1, 0, -1] )
		queue = [ (x,y) ]
		visited[x][y] = True
		while queue:
			front = queue.pop(0)
			for p in direction:
				np = (front[0]+p[0], front[1]+p[1])
				if self.isValid(np, m, n) and grid[np[0]][np[1]]=='1' and not visited[np[0]][np[1]]:
					visited[np[0]][np[1]] = True
					queue.append(np)
	def isValid(self, np, m, n):
		return np[0]>=0 and np[0]<m and np[1]>=0 and np[1]<n

grid = ["11110", "11010", "11000", "00000"]

grid1 = ["1", "1", "0", "1", "0"]
grid2 = ["11010"]
grid3 = ["0"]

grid4 = ["111", "101", "111"]

solution = Solution()

print (solution.numIslands(grid3))