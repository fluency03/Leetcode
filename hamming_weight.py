#!/usr/bin/python
# Hamming Weight Problems: 
# Write a function that takes an unsigned integer and 
# returns the number of ’1' bits it has

# import gmpy

class Solution:
	# @param n, an integer
	# @return an integer
	def hammingWeight(self, n):
		num = n
		hamming = 0
		while True:
			if num == 0: break
			num, rem = divmod(num, 2)
			if rem == 1:
				hamming += 1
		return hamming
	def hammingWeight_bin(self, n):
		return bin(n).count('1')
	def hammingWeight_and(self, n):
		hamming = 0
		while n > 0:
			n &= n - 1
			hamming += 1
		return hamming
	def hammingWeight_num(self, n):
		"""
		based on http://go.klaus.pw/hamming-weights_python
		bb should be of type bytes and should contain be a multiple of 8 bytes
		"""
		hamming = 0
		n -= (n >> 1) & 0x5555555555555555
		n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
		n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
		hamming += ((n * 0x0101010101010101) & 0xffffffffffffffff ) >> 56
		return hamming
	# def hammingWeight_popcount(self, n):
		# return gmpy.popcount(n)

solution = Solution()

print (solution.hammingWeight_bin(11))