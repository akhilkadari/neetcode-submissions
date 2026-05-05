class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count to list of anagrams

        for s in strs:
            count = [0] * 26 # a -> z
            for c in s:
                count[ord(c) - ord("a")]+=1 # a = 80, b = 81 
                                         # if we want 'a' at index 0 we do 80-80, 
                                         # if we want 'b' at index 1 we do 81-80
            res[tuple(count)].append(s)
        return list(res.values())
        