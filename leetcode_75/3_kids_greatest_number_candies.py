
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        greatestNumber =max(candies)
        for c in candies:
            if c + extraCandies >= greatestNumber:
                result.append(True)
            else:
                result.append(False)
        return result

sln=Solution()
assert [True,True,True,False,True] ==sln.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
assert [True,False,False,False,False]  ==sln.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1)
assert [True,False,True]  ==sln.kidsWithCandies(candies = [12,1,12], extraCandies = 10)

