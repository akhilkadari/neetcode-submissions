class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ns = ""
        for c in s:
            if c.isalnum():
                ns += c
        ns = ns.lower()
        L = 0
        R = len(ns) - 1

        while L < R:
            if ns[L] != ns[R]:
                return False
            L+=1
            R-=1
        return True
        