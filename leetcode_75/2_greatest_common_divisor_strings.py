
"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that 
x divides both str1 and str2.
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        print(f"str1 = {str1}; str2 = {str2}")
        print(f"len1 = {len1}; len2 = {len2}")
        def isDivisor(sublen):
            print(f"\n\nlen1 % sublen = {len1 % sublen}")
            print(f"len2 % sublen = {len2 % sublen}")
            
            if len1 % sublen or len2 % sublen:
                return False
                
            print(f"len1 // sublen = {len1 // sublen}")
            print(f"len2 // sublen = {len2 // sublen}")
            
            f1, f2 = len1 // sublen , len2 // sublen
            
            print(f"str1[:sublen] * f1 = {str1[:sublen] * f1}")
            print(f"str1[:sublen] * f2 = {str1[:sublen] * f2}")
            
            return str1[:sublen] * f1 == str1 and str1[:sublen] * f2 == str2
            
        for sublen in range(min(len1, len2), 0 , -1):
            if isDivisor(sublen):
                return str1[:sublen]
        return ""

soln = Solution()
x = soln.gcdOfStrings("ABABAB", "ABAB")
print(x)

assert soln.gcdOfStrings("ABCABC", "ABC") == "ABC"
assert soln.gcdOfStrings("ABABAB", "ABAB") == "AB"
assert soln.gcdOfStrings("LEET", "CODE") == ""

