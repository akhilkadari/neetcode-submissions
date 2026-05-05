class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            L, R = 0, len(row)-1

            while L<=R:
                mid=(L+R)//2
                if target>row[mid]:
                    L=mid+1
                elif target<row[mid]:
                    R=mid-1
                else:
                    return True
        return False