class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = -1
        while low <= high:
            k = (low + high)//2
            total_hours = sum([math.ceil(pile/k) for pile in piles])
            if total_hours > h:
                low = k+1
            elif total_hours <= h:
                ans = k
                high = k - 1

        return ans
        