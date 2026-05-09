class Solution:
    # approach 1
    # encoding:
    # list = ["hello", "world"]
    # - string = '5#hello5#world'

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + '#' + s
        return string
        
    # approach 1
    # decoding:
    # s = '5#hello5#world'
    # - i = 0
    # - loop through string
    #     - j = i
    #     - while j != '#'
    #       - j += 1
    #     - get length
    #     - move i to the beginning of the string (j+1)
    #     - move j to the end of the string (i+length)
    #     - append this word to the resulting list
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        return res

