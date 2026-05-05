class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currLength = 0
        L = 0
        res = 0
        
        for R in range(len(s)):
            for i in range(L, R):
                if s[i] == s[R]:
                    L = i + 1
                    break
            res = max(res, R-L+1)
        return res