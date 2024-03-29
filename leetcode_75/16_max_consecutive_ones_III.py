
"""
Given a binary array nums and an integer k, return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.
"""

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        count_flips = j = 0
        
        for start_index, v in enumerate(nums):
            if v == 0:
                count_flips += 1
            
            while count_flips > k:  ##### THIS ONLY TRIGGERED WHEN NUM FLIPS EXCEEDS 'k'
                if nums[j] == 0:
                    count_flips -= 1
                j += 1
            print(f"\n### Iter start_index = {start_index}; .... j = {j}; .... ans = {ans}; .... start_index - j + 1 = {start_index - j + 1}")
            ans = max(ans, start_index - j + 1)
        return ans
        
soln = Solution()
assert soln.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2) == 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


assert soln.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3) == 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
