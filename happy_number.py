#!/usr/bin/python
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive 
# integer, replace the number by the sum of the squares of its digits, and repeat the process 
# until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does 
# not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^
# 2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution:
	# @param {integer} n
	# @return {boolean}
	def isHappy(self, n):
		string_n = str(n)
		list_n = []
		list_n.append(n)
		sum_n = sum(int(i)*int(i) for i in string_n) 
		while True:
			if sum_n == 1:
				return True
			if sum_n not in list_n:
				list_n.append(sum_n)
			else:
				return False
			string_n = str(sum_n)
			sum_n = sum(int(i)*int(i) for i in string_n)


solution = Solution()

print (solution.isHappy(7))