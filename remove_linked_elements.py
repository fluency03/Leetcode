#!/usr/bin/python
# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
# @param {ListNode} head
# @param {integer} val
# @return {ListNode}
	def removeElements(self, head, val):
		p = ListNode(0)
		q = ListNode(0)
		lead = ListNode(0)
		lead.next = head
		p = lead
		q = head
		while q != None:
			if q.val is val:
				p.next = q.next
			else:
				p = p.next
			q = q.next
		return lead.next

solution = Solution()

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(1)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8


print (node1.next)

result = solution.removeElements(node1, 1)

while True:
	print (result.val)
	if result.next == None:
		break
	else:
		result = result.next