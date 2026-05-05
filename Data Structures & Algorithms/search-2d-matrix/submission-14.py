class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        arrayToSearch = []

        while L<=R:
            mid = (L+R) // 2
            row = matrix[mid]
            arrayToSearch = row
            if target < row[0]:
                R = mid-1
            elif target > row[-1]:
                L = mid+1
            else:
                break

        print(arrayToSearch)
        L, R = 0, len(arrayToSearch)-1

        while L<=R:
            mid = (L+R)//2
            if arrayToSearch[mid] < target:
                L = mid+1
            elif arrayToSearch[mid] > target:
                R = mid-1
            else:
                return True
        return False