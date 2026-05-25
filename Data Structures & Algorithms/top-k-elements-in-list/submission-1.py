class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: frequency count
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: build buckets (index = frequency)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, f in freq.items():
            buckets[f].append(num)

        # Step 3: collect top k
        res = []
        for f in range(n, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
        