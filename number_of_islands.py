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
		if len(grid)==0 or len(grid[0])==0 or grid==None:
			return 0
		island = 0
		# pre = 0
		for line in grid:
			pre = '0'
			for i in range(len(line)):
				if line[i]=='1' and pre=='0':
					island += 1
				pre = line[i]
		# print (island)
		connection = []
		pre_line = grid[0]
		for line in grid[1:]:
			connect = (int(pre_line[i]) and int(line[i]) for i in range(len(line)))
			connection.append(list(connect))
			pre_line = line
		# print (connection)
		merge = 0
		# pre = 0
		for line in connection:
			pre = 0
			for point in line:
				if point==1 and pre==0:
					merge += 1
				pre = point
		# print (island, merge)
		if island != 0 and island==merge:
			return 1
		return island-merge         

grid = ["11110", "11010", "11000", "00000"]

grid1 = ["1", "1", "0", "1", "0"]
grid2 = ["11010"]
grid3 = ["0"]

grid4 = ["111", "101", "111"]

solution = Solution()

print (solution.numIslands(grid3))