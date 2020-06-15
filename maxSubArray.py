"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        currSum = nums[0]
        maxSum = nums[0]
        for x in nums[1:]:
            currSum = max(x, currSum +x)
            maxSum = max(maxSum, currSum)
        return maxSum
        