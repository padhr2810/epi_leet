
"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 
0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.
"""



class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
         
        ##### METHOD 1:
        f = [0] + flowerbed + [0]
        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n-=1
        return n <= 0


        ##### METHOD 2:
        empty = 0 if flowerbed[0] else 1 
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1

        n -= (empty) // 2
        return n <= 0 
        
soln = Solution()
assert soln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1) == True 
assert soln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2) == False  



