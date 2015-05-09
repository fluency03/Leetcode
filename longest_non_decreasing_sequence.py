#!/usr/bin/python
# Let’s define a state i as being the longest non-decreasing sequence which has its last 
# number A[i] . This state carries only data about the length of this sequence. Note that 
# for i<j the state i is independent from j, i.e. doesn’t change when we calculate state j. 
# Let’s see now how these states are connected to each other. Having found the solutions 
# for all states lower than i, we may now look for state i. At first we initialize it 
# with a solution of 1, which consists only of the i-th number itself. Now for each j<i 
# let’s see if it’s possible to pass from it to state i. This is possible only when 
# A[j]≤A[i] , thus keeping (assuring) the sequence non-decreasing. So if S[j] 
# (the solution found for state j) + 1 (number A[i] added to this sequence which ends 
# with number A[j] ) is better than a solution found for i (ie. S[j]+1>S[i] ), we make 
# S[i]=S[j]+1. This way we consecutively find the best solutions for each i, until last state N.

# Let’s see what happens for a randomly generated sequence: 5, 3, 4, 8, 6, 7:


# I		The length of the longest	The last sequence i from
# 		non-decreasing sequence		which we "arrived"
# 		of first i numbers			to this one
# 1		1							1 (first number itself)
# 2		1							2 (second number itself)
# 3		2							2
# 4		3							3
# 5		3							3
# 6		4							5

class Solution:
	# enter parameter: an array of integers;
	# output: the length of longest non-decreasing sequence
	def longestNonDecreasingSeq(self, seq):
		s = [1]*len(seq)
		choice = [[]] * len(seq)
		# choice[0].append(seq[0])
		for i in range(len(seq)):
			for j in range(i):
				if seq[j] <= seq[i]:
					if s[j]+1 > s[i]:
						s[i] = s[j]+1
						# choice[i] = choice[j]+[seq[i]]
		print (s)
		# print (choice)
		return s[len(seq)-1]


solution = Solution()

array = [5, 3, 4, 8, 6, 7]
# array = [1, 2, 3, 4, 5, 10, 6, 7]

print (solution.longestNonDecreasingSeq(array))