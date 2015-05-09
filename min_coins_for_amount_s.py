#!/usr/bin/python
# Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. 
# Find the minimum number of coins the sum of which is S (we can use as many coins of 
# one type as we want), or report that it’s not possible to select coins in such a way 
# that they sum up to S.

class Solution:
	# coins: an array of integer values
	# sum: an integer
	def minCoins(self, coins, s):
		Min = [float('inf')] * (s+1)
		Min[0] = 0
		choice = [[]] * (s+1)
		for i in range(1, s+1):
			for j in range(len(coins)):
				if ( coins[j]<=i and Min[i-coins[j]]<Min[i] ):
					Min[i] = Min[i-coins[j]]+1
					choice[i] = choice[i-coins[j]] + [coins[j]]
		print (Min)
		print (choice)
		if Min[s] == float('inf'):
			print ("Not possible!!!")
		else:
			return Min[s]
	def minCoins1(self, coins, s):
		Min = [float('inf')] * (s+1)
		Min[0] = 0
		choice = [[]] * (s+1)
		for j in range(len(coins)):
			for i in range(0, s+1):
				if (i+coins[j]) <= s and Min[i]<Min[i+coins[j]]:
					Min[i+coins[j]] = Min[i]+1
					choice[i+coins[j]] = choice[i] + [coins[j]]
		print (Min)
		print (choice)
		if Min[s] == float('inf'):
			print ("Not possible!!!")
		else:
			return Min[s]





solution = Solution()

a = [2, 3, 5]
s = 10

print (solution.minCoins(a, s))

# print 