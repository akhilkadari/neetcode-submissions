class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longesSub = set()
        length = 0 
        L = 0

        for R in range(len(s)):
            while s[R] in longesSub:
                longesSub.remove(s[L])
                L+=1
            longesSub.add(s[R])
            length = max(length, R-L+1)
        return length            