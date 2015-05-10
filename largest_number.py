#!/usr/bin/python

# Given a list of non negative integers, arrange them such that they form 
# the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string 
# instead of an integer.

class Solution:
	# @param {integer[]} nums
	# @return {string}
	def largestNumber(self, nums):
		strings = list(map(str, nums))
		formed = [None]
		formed[0] = strings[0]
		for a in strings[1:]:
			i = 0
			temp = formed[:]
			for b in temp:
				if self.bit_sort(a, b):
					formed.insert(i, a)
					break
				else:
					i += 1
				if i==len(temp):
					formed.insert(i, a)
		if formed[0] == '0':
			return '0'
		else:
			return (''.join(map(str, formed)))
	def bit_sort(self, a, b):
		ab = a+b
		ba = b+a
		if ab>=ba:
			return True
		else:
			return False

# ------------------------------------------------------------------------

import functools

# Another solution
class SolutionRef:
	# @param num, a list of integers
	# @return a string
	def largestNumber(self, num):
		num = sorted([str(x) for x in num], key=functools.cmp_to_key(self.compare))
		# or fo the folowing: 
		# num = sorted([str(x) for x in num], key=cmp_to_key(self.compare))
		ans = ''.join(num).lstrip('0')
		return ans or '0'
	def compare(self, a, b):
		return [1, -1][a + b > b + a]

# This def is used to handle cmp to key, since cmp cannot be used in Python3
# For instance, l.sort(cmp=mycmp) converts to l.sort(key=cmp_to_key(mycmp)).

# def cmp_to_key(mycmp):
#     'Convert a cmp= function into a key= function'
#     class K(object):
#         def __init__(self, obj, *args):
#             self.obj = obj
#         def __lt__(self, other):
#             return mycmp(self.obj, other.obj) < 0
#         def __gt__(self, other):
#             return mycmp(self.obj, other.obj) > 0
#         def __eq__(self, other):
#             return mycmp(self.obj, other.obj) == 0
#         def __le__(self, other):
#             return mycmp(self.obj, other.obj) <= 0  
#         def __ge__(self, other):
#             return mycmp(self.obj, other.obj) >= 0
#         def __ne__(self, other):
#             return mycmp(self.obj, other.obj) != 0
#     return K




solution = SolutionRef()

nums = [3, 30, 34, 5, 9]

print (solution.largestNumber(nums))