#!/usr/bin/python
# House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain 
# amount of money stashed, the only constraint stopping you from robbing each of them is that 
# adjacent houses have security system connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine
# the maximum amount of money you can rob tonight without alerting the police.

class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def rob(self, nums):
		'''recursively calculate amount(i):
		amount(i-1) and amount(i-2)+num[i]'''
		amountA, amountB = 0, 0
		for num in nums:
			amountA, amountB = max(amountA, amountB), amountA + num
		return max(amountA, amountB)
	def rob_2(self, nums):
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return max(nums[0], nums[1])
		amount = [0 for i in range(len(nums))]
		amount[0] = nums[0]
		amount[1] = max(nums[0], nums[1])
		for i in range(2,len(nums)):
			amount[i] = max(amount[i-1], amount[i-2]+nums[i])
		return amount[-1]


solution = Solution()

print(solution.rob([2,1,1,2]))