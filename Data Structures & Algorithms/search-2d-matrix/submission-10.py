class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L,R=0,len(matrix)-1
        row = -1
        arr=[]
        while L<=R:
            mid=(L+R)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0]<target:
                row = mid
                L=mid+1
            else:
                R=mid-1
        if row == -1:
            return False

        arr = matrix[row]
        print(arr)
        if target == arr[0]:
            return True
      

        L1,R1 = 0,len(arr)-1
        while L1<=R1:
            mid1=(L1+R1)//2
            if target>arr[mid1]:
                L1=mid1+1
            elif target<arr[mid1]:
                R1=mid1-1
            else:
                return True
        return False
