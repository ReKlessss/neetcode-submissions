class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        arr = []

        while l <= r:
            m = (l + r) // 2
            arr = matrix[m]

            if arr[0] > target:
                r = m - 1
            elif arr[-1] < target:
                l = m + 1
            else:
                l, r = 0, len(arr) - 1
                break
        
        while l <= r:
            m = (l + r) // 2
            guess = arr[m]

            if guess > target:
                r = m - 1
            elif guess < target:
                l = m + 1
            else:
                return True
        
        return False




        
        
        return False