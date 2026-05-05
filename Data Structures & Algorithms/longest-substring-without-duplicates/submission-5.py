class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubs = ""
        L = 0
        length = float("-inf")

        for R in range(len(s)):
            while longestSubs and s[R] in longestSubs:
                L +=1
                longestSubs = longestSubs[1:]
            longestSubs += s[R]
            length = max(length, len(longestSubs))
        return 0 if length == float("-inf") else length

            