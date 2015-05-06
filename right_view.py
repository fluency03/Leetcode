#!/usr/bin/python
# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
# 
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  /     
# 6               <---
# You should return [1, 3, 4, 6].


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[]}
	def rightSideView(self, root):
		sideview = []
		if root == None:
			return sideview
		# sideview.append(root.val)
		sideview = self.search(root)
		return sideview
	def search(self, node):
		if node == None:
			return []
		if node.left == None and node.right == None:
			return [node.val]
		left = self.search(node.left)
		right = self.search(node.right)
		print (left, right)
		if len(right)>=len(left):
			return ([node.val] + right)
		else:
			remain = left[len(right):]
			return ([node.val]+right+remain)
	def rightSideView1(self, root):
		ans = []
		if root is None:
			return ans
		queue = [root]
		while queue:
			size = len(queue)
			for r in range(size):
				top = queue.pop(0)
				if r == 0:
					ans.append(top.val)
				if top.right:
					queue.append(top.right)
				if top.left:
					queue.append(top.left)
		return ans


# a = [1, 2, 3, 4, 5]
# a = [1]

# b = a[-1:]

# print (b)
# print (a+b)

solution = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)
node5 = TreeNode(4)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.right = node4
node3.right = node5
node4.left = node6

result = solution.rightSideView1(node1)

print (list(result))
