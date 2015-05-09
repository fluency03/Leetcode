#!/usr/bin/python
# A table composed of N x M cells, each having a certain quantity of apples, is given. 
# You start from the upper-left corner. At each step you can go down or right one cell. 
# Find the maximum number of apples you can collect.

# From above, a recurrent relation can be easily obtained:
# S[i][j]=A[i][j] + max(S[i-1][j], if i>0 ; S[i][j-1], if j>0) (where i represents the 
# row and j the column of the table , its left-upper corner having coordinates {0,0} ; 
# and A[i][j] being the number of apples situated in cell i,j).

# S[i][j] must be calculated by going first from left to right in each row and process 
# the rows from top to bottom, or by going first from top to bottom in each column and 
# process the columns from left to right.

class Solution:
	# input: a 2-D array with non-negative integers
	# output: maximum amount, an integer
	def maxAmountApples(self, A):
		N = len(A)
		M = len(A[0])
		s = [[0]*M]*N
		for i in range(N):
			for j in range(M):
				pre1 = s[i][j-1] if j>0 else 0
				pre2 = s[i-1][j] if i>0 else 0
				s[i][j] = A[i][j] + max(pre1, pre2, 0)
				print (i, j, s[i][j])
		return s[N-1][M-1]


solution = Solution()

a = [[4, 6, 7, 8], 
	 [7, 5, 3, 1], 
	 [9, 2, 4, 6], 
	 [9, 0, 5, 1], 
	 [4, 6, 3, 8], 
	 [8, 0, 2, 4]]

print (solution.maxAmountApples(a))