
"""
type: greedy // array.
"""


"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
"""

"""
The time complexity of the given code is O(n) where n is the number of elements in the nums list. 
This is because the code iterates through the entire nums list once with a single loop, 
and within each iteration, it performs a constant number of operations.

The space complexity of the given code is O(1) regardless of the size of the input list. 
It uses only two extra variables, mi and mid, which consume a constant amount of space.
"""

"""
Problem Description
The problem gives us an array of integers, nums, and asks us to determine if it is possible to 
find a sequence of three elements, where each element comes after the previous one in the order 
they appear in the array (i.e., they have increasing indices), and each element is greater than the 
one before it in this sequence. This sequence should satisfy the condition nums[i] < nums[j] < nums[k], 
where i, j, and k are the indices of these elements in the array, such that i < j < k. If such a sequence exists in nums, 
the function should return true, otherwise, it should return false.

This can be visualized as checking if there's an ascending subsequence of at least three numbers within the original array. 
It's essentially a question about identifying a pattern within a sequence without reordering it or changing the values.

Intuition
To arrive at the solution efficiently, instead of looking for the whole triplet right away, 
we can keep track of the smallest number we have encountered so far (mi) 
and a middle number that is greater than mi but smaller than any potential third number (mid). 
As we iterate through the array, we can update these two numbers whenever possible. 
The idea here is to maintain the lowest possible values for mi and mid as we move forward, 
giving us the best chance to find a number that would be greater than both, thus forming our triplet.

If the current number (num) is less than or equal to mi, it becomes the new mi 
because we're always interested in the smallest starting point of the potential triplet.
If num is greater than mi but less than mid, we have found 
a possible middle part of our triplet, so we set mid to this new number.
If num is greater than mid, this means we have successfully found a triplet 
(because num is greater than both mi and mid, which also implies that mi is less than mid), 
and we can return true.
This efficient approach uses a greedy-like method to continuously look for the most optimal mi and mid 
with the hope of finding a third number that could fit the sequence. 
It does so using a linear scan and constant extra space, without the need for sorting or extra arrays.

Learn more about Greedy patterns.

Solution Approach
The Reference Solution Approach begins with the creation of two variables: mi and mid, 
both initialized to inf (infinity). Here's the reasoning for each line of code:

mi and mid serve as placeholders to store the smallest and middle elements of the potential increasing triplet subsequence. 
By initializing them to infinity, it ensures that any number in the array will be smaller, allowing for proper updating of these variables.
The main algorithm unfolds within a single pass through the array of numbers (nums):

A for loop iterates through the nums array.
For each num in nums, there is a series of checks and updates:
if num > mid: This is the condition that tells us we have found a valid triplet. 
        If the current num is greater than our mid value, then we already have a mi which is less than mid, and hence, we have found a sequence where mi < mid < num. We return True immediately.
if num <= mi: If the current num is smaller than or equal to the current smallest value mi, 
        it means that we can potentially start a new triplet sequence with this num as the smallest element, thus we update mi with the value of num.
else: If the current num is greater than mi and not greater than mid, 
        it fits between the mi and mid, so we update the mid to be num since it could potentially be the middle element of a valid triplet.
As the for loop continues, mi and mid are updated accordingly until either a valid triplet is found—
        causing the function to return True—or the algorithm completes the array iteration without finding a triplet, 
        resulting in a return value of False.

It's important to note that the code uses a greedy approach to always maintain the smallest possible values for mi and mid 
    as it iterates over nums. By consistently updating these with the smallest possible values at each step, 
    it optimizes the chance of finding a valid triplet later in the array. No additional data structures are necessary, 
    making this solution notably efficient with O(n) time complexity (due to single iteration through the array) 
    and O(1) space complexity (using only two extra variables).
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ### TRICK - DONT NEED ALL 3 TO BE TOGETHER
        ###     CAN HAVE OTHERS IN BETWEEN
        ###     SO SET SMALL AND MID TO INF.

        
        smaller_of_3, mid_of_3 = float('inf'), float('inf')
        for num in nums:            ### CHECK ONE NUM AT A TIME.
        
            if num > mid_of_3:          ### FOUND THE BIGGEST.
                print(f"small = {smaller_of_3}; mid = {mid_of_3}; big = {num}")
                return True             ### MUST BE ASCENDING ORDER - SO ONLY THIRD (BIGGEST) NUM CAN TRIGGER "return True"
            
            if num <= smaller_of_3:         ### WHEN FIND A NEW "smallest" DO 2 THINGS.
                smaller_of_3 = num          ### 1. SET THE SMALLEST. 2. RESET MID TO INF. 
                #mid_of_3 = float('inf')     
                
            else:                           ### OTHERWISE FOUND THE MIDDLE OBVIOUSLY.
                mid_of_3 = num
            
        return False
    
soln = Solution()
assert soln.increasingTriplet(nums = [1,2,3,4,5]) == True
# Explanation: Any triplet where i < j < k is valid.

assert soln.increasingTriplet(nums = [5,4,3,2,1]) == False 
# Explanation: No triplet exists.

assert soln.increasingTriplet(nums = [2,1,5,0,4,6]) == True  
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

assert soln.increasingTriplet(nums = [2,1,5,0,6]) == True  
#   Explanation: values = 2, 5, 6 ... ie indices 0, 2, 4

assert soln.increasingTriplet(nums = [2,3,1,5,0,4]) == True   
assert soln.increasingTriplet(nums = [2,3,3,5,0,4]) == True  
