class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            if op == "+":
                ans.append(sum(map(int, ans[-2:])))
            elif op == "C":
                ans.pop(-1)
            elif op == "D":
                ans.append(ans[-1]*2)
            else:
                ans.append(int(op))

        return sum(ans)
        