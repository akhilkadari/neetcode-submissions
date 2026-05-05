class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubs = set()
        L = 0
        length = float("-inf")

        for R in range(len(s)):
            while s[R] in longestSubs:
                longestSubs.remove(s[L])
                L +=1
            longestSubs.add(s[R])
            length = max(length, R-L+1)
        return 0 if length == float("-inf") else length

            