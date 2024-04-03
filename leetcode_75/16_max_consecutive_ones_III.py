
"""
Given a binary array "nums" and an integer "flips_allowed" , return the maximum number of 
consecutive 1's in the array if you can flip at most 'flips_allowed' 0's.
"""

class Solution(object):
    def longestOnes(self, nums, flips_allowed):
        """
        :type nums: List[int]
        :type flips_allowed: int
        :rtype: int
        """
        ans = 0
        count_flips = j = 0
        
        for start_index, v in enumerate(nums):
            if v == 0:
                count_flips += 1
            
            while count_flips > flips_allowed:  ##### THIS ONLY TRIGGERED WHEN NUM FLIPS EXCEEDS 'flips_allowed'
                if nums[j] == 0:
                    count_flips -= 1
                j += 1
            print(f"\n### Iter start_index = {start_index}; .... j = {j}; .... ans = {ans}; .... start_index - j + 1 = {start_index - j + 1}")
            ans = max(ans, start_index - j + 1)
        return ans
        
soln = Solution()
assert soln.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], flips_allowed = 2) == 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


assert soln.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], flips_allowed = 3) == 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
