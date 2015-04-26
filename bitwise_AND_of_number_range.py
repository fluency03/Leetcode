#!/usr/bin/python
# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# return the bitwise AND of all numbers in this range, inclusive.

# For example, given the range [5, 7], you should return 4.

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        offset = 0
        while (m!=0 and n!=0):
            if m == n:
            	return m<<offset
            m >>= 1
            n >>= 1
            offset += 1
        return 0

solution = Solution()

print (solution.rangeBitwiseAnd(20000,2147483647))