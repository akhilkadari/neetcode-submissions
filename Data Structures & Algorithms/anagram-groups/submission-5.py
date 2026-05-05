class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                # a = 80 -> 80 - 80 = 0
                # b = 81 -> 81 - 80 = 1
            res[tuple(count)].append(s)

        return list(res.values())