class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapC = {}
        for c in s:
            if c not in mapC:
                mapC[c] = 1
            else:
                mapC[c]+=1
        

        mapT = {}
        for c in t:
            if c not in mapT:
                mapT[c] = 1
            else:
                mapT[c]+=1
        
        if mapT == mapC:
            return True
        else:
            return False
        