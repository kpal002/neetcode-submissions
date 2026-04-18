class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0]*n
        right = -1
        for i in range(n-1,-1,-1):
            res[i] = right
            right = max(arr[i],right)
        return res
        