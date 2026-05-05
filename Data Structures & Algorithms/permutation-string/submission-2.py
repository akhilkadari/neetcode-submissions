class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0] * 26
        for c in s1:
            c1[ord(c) - ord('a')]+=1
        
        k = len(s1)
        l = 0
        c2 = [0] * 26

        for r in range(len(s2)):
            c2[ord(s2[r]) - ord('a')] += 1

            if r-l+1 > k:
                c2[ord(s2[l])-ord('a')]-=1
                l+=1
            
            if r-l+1 == k and c1 == c2:
                return True
        return False
