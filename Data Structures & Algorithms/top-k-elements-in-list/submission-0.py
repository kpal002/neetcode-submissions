class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        top_k = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:k])
        return list(top_k.keys())

        