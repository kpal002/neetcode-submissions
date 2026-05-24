class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_diff = 0
        for val in prices:
            if val < lowest:
                lowest = val

            current_diff = val - lowest
            if current_diff > max_diff:
                max_diff = current_diff

        return max_diff
