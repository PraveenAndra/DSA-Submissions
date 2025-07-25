class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        found = False
        while top <= bottom:
            mid = top + (bottom-top)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                found = True
                break
            if matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        
        left,right = 0,len(matrix[0])
        if not found:
            return False
        while left <= right:
            mid1 = left + (right-left)//2
            if matrix[mid][mid1] == target:
                return True
            if matrix[mid][mid1] < target:
                left = mid1+1
            else:
                right =mid1 -1
        return False


        