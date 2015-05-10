#!/usr/bin/python
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

# Note:
# You may not engage in multiple transactions at the same time (i.e., you must sell the 
# stock before you buy again).

class Solution:
	# @param {integer} k
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, k, prices):
		# 问题的实质是从长度为n的prices数组中挑选出至多2 * k个元素，组成一个交易（买卖）序列。
		# 交易序列中的首次交易为买入，其后卖出和买入操作交替进行。
		# 总收益为交易序列中的偶数项之和 - 奇数项之和。
		# ch = [1, -1]
		size = len(prices)
		if k >= size/2:
			return self.quickSolve(size, prices)
		profit = [ None ]*(2*k+1)
		profit[0] = 0
		for i in range(size):
			for j in range(min(2*k, i+1), 0, -1):
				profit[j] = max(profit[j], profit[j-1]+prices[i]*[1, -1][j%2]) 
		return max(profit)
	def quickSolve(self, size, prices):
		'''Greedy'''
		# 由于直接采用动态规划会返回Time Limit Exceeded，可以针对题目部分样例做出下面的优化：
		# 令最大交易次数为k，数组长度为size；
		# 则当k > size / 2时，问题可以转化为：Best Time to Buy and Sell Stock II
		sum = 0
		for x in range(size-1):
			if prices[x+1] > prices[x]:
				sum += prices[x+1]-prices[x]
		return sum

solution = Solution()

# prices = [5, 6, 3, 8 ,9, 12, 6, 9, 10]
prices = [1, 2]

print (solution.maxProfit(1, prices))