class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = 0
        i = 0
        while i < len(matrix):
            if target < matrix[i][0]:
                target_row = i - 1
                break
            target_row = i
            i += 1
        L, R = 0, len(matrix[target_row]) - 1
        ans = -1
        while L <= R:
            mid = (L + R) // 2
            if target > matrix[target_row][mid]:
                L = mid + 1
            elif target < matrix[target_row][mid]:
                R = mid - 1
            else:
                ans = mid
                break

        if ans != -1:
            return True
        else:
            return False