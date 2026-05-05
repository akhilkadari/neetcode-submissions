class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for list in board:
            r_map = {}
            for num in list:
                if num in arr:
                    if num not in r_map:
                        r_map[num] = 1
                    else:
                        return False
        
        i = 0
        while i < 9:
            c_map = {}
            for list in board:   
                if list[i] in arr:
                    if list[i] not in c_map:
                        c_map[list[i]] = 1
                    else:
                        return False
            i+=1
        
        for rs in [0,3,6]:
            for cs in [0,3,6]:
                map = {}
                for i in range(3):
                    for j in range(3):
                        num = board[rs+i][cs+j]
                        if num in arr:
                            if num not in map:
                                map[num] = 1
                            else:
                                return False
        return True

       


        
                