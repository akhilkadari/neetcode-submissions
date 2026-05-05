class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
    #     for list in board:
    #         r_map = {}
    #         for num in list:
    #             if num in arr:
    #                 if num not in r_map:
    #                     r_map[num] = 1
    #                 else:
    #                     return False
        
    #     i = 0
    #     while i < 9:
    #         c_map = {}
    #         for list in board:   
    #             if list[i] in arr:
    #                 if list[i] not in c_map:
    #                     c_map[list[i]] = 1
    #                 else:
    #                     return False
    #         i+=1
        
    #     for rs in [0,3,6]:
    #         for cs in [0,3,6]:
    #             map = {}
    #             for i in range(3):
    #                 for j in range(3):
    #                     num = board[rs+i][cs+j]
    #                     if num in arr:
    #                         if num not in map:
    #                             map[num] = 1
    #                         else:
    #                             return False
    #     return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range (9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or 
                   board[r][c] in col[c] or 
                   board[r][c] in squares[(r//3,c//3)]):
                    return False
                col[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True















