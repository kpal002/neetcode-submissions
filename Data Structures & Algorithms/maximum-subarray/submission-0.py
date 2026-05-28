class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_max = 0

        for x in nums:
            current_max += x
            if current_max > max_sum:
                max_sum = current_max

            if current_max < 0:
                current_max = 0

        return max_sum 
        