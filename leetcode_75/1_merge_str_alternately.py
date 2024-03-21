
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m=len(word1)
        n=len(word2)
        i=0
        j=0
        result=[]
        while i<m or j<n:
            if i<m:
              result+=word1[i]
              i+=1
            if j<n:
                result+=word2[j]
                j+=1
        return "".join(result)


soln = Solution()
x = soln.mergeAlternately("ACE", "BDF")
print(x)
x = soln.mergeAlternately("ACE", "BDFGHI")
print(x)
x = soln.mergeAlternately("1356", "24")
print(x)