
"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

"""

class Solution:
    def asteroidCollision(self, asteroids) :
        stk = []
        for x in asteroids:
            if x > 0:
                stk.append(x)
            else:
                while stk and stk[-1] > 0 and stk[-1] < -x:
                    stk.pop()
                if stk and stk[-1] == -x:
                    stk.pop()
                elif not stk or stk[-1] < 0:
                    stk.append(x)
        return stk
        
soln = Solution()

assert soln.asteroidCollision(asteroids = [5,10,-5]) == [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

assert soln.asteroidCollision(asteroids = [8,-8]) == []
# Explanation: The 8 and -8 collide exploding each other.

assert soln.asteroidCollision([10,2,-5]) == [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
