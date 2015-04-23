#!/usr/bin/python
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

from collections import deque

class Solution:
	# @param nums, a list of integer
	# @param k, num of steps
	# @return nothing, please modify the nums list in-place.
	def rotate(self, nums, k):
		for i in range(k):
			nums.insert(0, nums.pop())
		return nums
# --------------------------------------------------------------------------------
	def rotate_deque(self, nums, k):
		'''using collections.deque'''
		nums = deque(nums)
		nums.rotate(k)
		return list(nums)
# --------------------------------------------------------------------------------
	def rotate_reverse(self, nums, k):
		# 以n - k为界，分别对数组的左右两边执行一次逆置；然后对整个数组执行逆置。
		'''using reverse'''
		n = len(nums)
		k %= n
		self.reverse(nums, 0, n - k)
		self.reverse(nums, n - k, n)
		self.reverse(nums, 0, n)
		return nums
	def reverse(self, nums, start, end):
		for x in range(start, int((start + end)/2)):
			nums[x] ^= nums[start + end - x - 1]
			nums[start + end - x - 1] ^= nums[x]
			nums[x] ^= nums[start + end - x - 1]
# --------------------------------------------------------------------------------
	def rotate_move(self, nums, k):
		# 将数组元素依次循环向右平移k个单位
		n = len(nums)
		idx = 0
		distance = 0
		cur = nums[0]
		for x in range(n):
			next = (idx + k) % n
			temp = nums[next]
			nums[next] = cur
			idx = next
			cur = temp
			distance = (distance + k) % n
			if distance == 0:
				idx = (idx + 1) % n
				cur = nums[idx]
		return nums

solution = Solution()

print (solution.rotate([1,2,3,4,5,6,7], 3))
