#!/usr/bin/python
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify 
# repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur 
# more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

class Solution:
	"""docstring for Solution"""
	# @param {string} s
	# @return {string[]}
	def findRepeatedDnaSequences(self, s):
		# too slow !!!!!
		if len(s) <= 10:
			return []
		repeated = []
		length = len(s)
		seqs = []
		for i in range(length-9):
			seq = s[i:i+10]
			seqs.append(seq)
		print (seqs)
		for q in seqs:
			flag = 0
			for p in seqs:
				if q == p:
					flag += 1
					# seqs.remove(p)
			if flag >= 2 and q not in repeated:
				repeated.append(q)
		return repeated
	def findRepeatedDnaSequences1(self, s):
		ans = []
		valCnt = dict()
		map = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
		sum = 0
		for x in range(len(s)):
			sum = (sum * 4 + map[s[x]]) & 0xFFFFF 
			# "& 0xFFFFF" is used to keep the last 10 letters' value
			if x < 9:
				continue
			valCnt[sum] = valCnt.get(sum, 0) + 1
			if valCnt[sum] == 2:
				ans.append(s[x - 9 : x + 1])
		return ans
	def findRepeatedDnaSequences2(self, s):
		# fastest one for now!  
		dict={}
		for i in range(len(s)-9):
			key=s[i:i+10]
			if key not in dict:
				dict[key]=1
			else:
				dict[key]+=1
		res=[]
		for elem in dict:
			if dict[elem]>1:
				res.append(elem)
		return res


solution = Solution()

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

print (solution.findRepeatedDnaSequences2(s))