class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            for n in arr:
                if n == target:
                    return True

        return False