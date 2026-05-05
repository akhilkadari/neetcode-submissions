class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0] * 26
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1

        k = len(s1)
        c2 = [0] * 26
        l = 0

        for r in range(len(s2)):
            c2[ord(s2[r]) - ord('a')] += 1

            if r-l+1 > k:
                c2[ord(s2[l])-ord('a')] -= 1
                l+=1
            
            if r-l+1 == k and c2 == c1:
                return True
            
        return False
    