class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1

        while L <= R:
            mid = (L + R) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                L = mid + 1
            else:
                R = mid - 1

        return False