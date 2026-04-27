class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i, j = 0, n - 1
        while i <= j:
            row = (i + j) // 2
            if target > matrix[row][-1]:
                i += 1
            elif target < matrix[row][0]:
                j -= 1
            else:
                break
        
        l, r = 0, m - 1
        while l <= r:
            index = (l + r) // 2
            if target == matrix[row][index]:
                return True
            elif target > matrix[row][index]:
                l += 1
            else:
                r -= 1
        
        return False