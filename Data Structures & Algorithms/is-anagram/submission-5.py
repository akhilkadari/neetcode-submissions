class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}

        for n in s:
            if n in mapS:
                mapS[n] += 1
            else:
                mapS[n] = 1
        
        mapT = {}

        for n in t:
            if n in mapT:
                mapT[n] += 1
            else:
                mapT[n] = 1
        
        return (mapS == mapT)
