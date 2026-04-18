class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range (len(operations)):
            if operations[i] == "+":
                ans.append(sum(map(int, ans[-2:])))
            elif operations[i] == "C":
                ans.pop(-1)
            elif operations[i] == "D":
                ans.append(ans[-1]*2)
            else:
                ans.append(int(operations[i]))

        return sum(ans)
        