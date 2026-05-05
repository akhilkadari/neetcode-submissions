class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        for l in s:
            if l not in mapS:
                mapS[l] = 1
            else:
                mapS[l] += 1
        mapT = {}
        for l in t:
            if l not in mapT:
                mapT[l] = 1
            else:
                mapT[l] += 1
        
        if mapS == mapT:
            return True
        return False