
"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smaller_of_3, mid_of_3 = float('inf'), float('inf')
        for num in nums:            ### CHECK ONE NUM AT A TIME.
            if num > mid_of_3:
                return True
            if num <= smaller_of_3:           ### THIS HAPPENS FIRST PASS. I.E. "mi" IS FIRST NUMBER.
                smaller_of_3 = num
            else:
                mid_of_3 = num
        return False
    
soln = Solution()
assert soln.increasingTriplet(nums = [1,2,3,4,5]) == True
# Explanation: Any triplet where i < j < k is valid.

assert soln.increasingTriplet(nums = [5,4,3,2,1]) == False 
# Explanation: No triplet exists.

assert soln.increasingTriplet(nums = [2,1,5,0,4,6]) == True  
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

