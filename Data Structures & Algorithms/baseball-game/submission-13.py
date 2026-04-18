class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        ans = []
        for i in range (n):
            if operations[i] == "+":
                ans.append(sum(map(int, ans[-2:])))
            elif operations[i] == "C":
                ans.pop(-1)
            elif operations[i] == "5":
                
                ans.append(5)
            elif operations[i] == "D":
                ans.append(ans[-1]*2)
            else:
                ans.append(int(operations[i]))
            print(operations[i])
            print(ans)

        return sum(ans)
        