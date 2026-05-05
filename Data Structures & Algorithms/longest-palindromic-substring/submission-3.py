class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        maxPalindrom = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l+=1
                    r-=1
                
                if l >= r and maxL < (j-i+1):
                    maxPalindrome = s[i : j + 1]
                    maxL = j - i + 1

        return maxPalindrome
            
        