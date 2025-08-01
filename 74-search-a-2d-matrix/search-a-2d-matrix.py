class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r,c = len(matrix),len(matrix[0])
        if r==0:
            return False
        left = 0
        right = r*c - 1
        while left <= right:
            mid = (left+right)//2
            pivot = matrix[mid//c][mid%c] 
            if pivot == target:
                return True
            else:
                if target < pivot:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
            