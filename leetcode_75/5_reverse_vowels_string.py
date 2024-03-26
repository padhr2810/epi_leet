class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        
        i, j = 0, len(s) - 1        ### pointers - forwards and backwards
        res_list = list(s)
        while i < j:
            while i < j and res_list[i] not in vowels:   ### similar to palindrome.
                i += 1                                      ### find vowel at start.
             
            while i < j and res_list[j] not in vowels:   ### find vowel at end.
                j -= 1

            if i < j:                              ### check again, not at halfway.
                res_list[i], res_list[j] = res_list[j], res_list[i]        ### swap
                i, j = i + 1, j - 1
        return "".join(res_list)
        
soln = Solution()
input_word = "who is there"
print(soln.reverseVowels(input_word) )
print(soln.reverseVowels("him no") )


