'''
Sliding Window technique
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Leetcode 438
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) <len(p) or len(s) == 0:
            return []
        letters= [0]*26
        final =[]
        for x in p:
            tmp = ord(x) -ord('a')
            letters[tmp] += 1
        
        diff = len(p)

        for x in range(len(p)):
            tmp = ord(s[x]) - ord('a')
            letters[tmp] -=1
            
            if letters[tmp] >= 0:
                diff -= 1
        if diff ==0:
            final.append(0)
        end = len(p)
        start =0
        while end <len(s):
            tmp = ord(s[start]) - ord('a')
            if letters[tmp] >= 0:
                diff +=1
            
            letters[tmp] +=1
            
            start += 1
            
            tmp = ord(s[end]) - ord('a')
            
            letters[tmp] -=1
            if letters[tmp] >= 0:
                diff -=1
            
            if diff == 0:
                final.append(start)
                
            end +=1
        return final