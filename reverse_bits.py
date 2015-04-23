#!/usr/bin/python
# Reverse bits of a given 32 bits unsigned integer.
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).

class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		n_bin = '{0:032b}'.format(n)
		return int(n_bin[::-1], 2)
	def reverseBits_normal(self, n):
		# 朴素解法
		'''normal way'''
		ans = 0
		for i in range(32):
			ans <<= 1
			ans |= n & 1
			n >>= 1
		return ans

solution = Solution()

print (solution.reverseBits(43261596))