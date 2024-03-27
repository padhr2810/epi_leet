"""
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums) :
        n = len(nums)
        ans = [0] * n
        left = right = 1
        for i, x in enumerate(nums):
            ans[i] = left
            left *= x
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
   
soln = Solution() 
assert soln.productExceptSelf(nums = [1,2,3,4]) == [24,12,8,6]
assert soln.productExceptSelf(nums = [-1,1,0,-3,3]) == [0,0,9,0,0]

