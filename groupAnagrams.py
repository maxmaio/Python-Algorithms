"""
Given an array of strings, group anagrams together.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp ={}
        tmp1= ""
        for i in strs:
            tmp1 = sorted(i)
            tmp = tuple(tmp1)
            dp[tmp] = dp.get(tmp, []) + [i]
        return dp.values()