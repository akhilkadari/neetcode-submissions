class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}

        for i in range(len(s)): 
            # mapS.get(s[i], 0) -> recieves the value at that key if it exists, else map it to 0
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        return mapT == mapS