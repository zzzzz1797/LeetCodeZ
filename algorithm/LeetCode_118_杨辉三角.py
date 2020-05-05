from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pass

    @classmethod
    def dp(cls, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [0 for i in range(i + 1)]
            row[0] = 1
            row[-1] = 1

            for j in range(1, i):
                row[j] = res[i - 1][j] + res[i - 1][j - 1]
            res.append(row)
        return res

    @classmethod
    def recursive(cls, numRows):

        def helper(n):
            if n == 0:
                return []
            if n == 1:
                return [[1]]
            last = helper(n - 1)
            last.append([1] + [last[-1][i - 1] + last[-1][i] for i in range(1, n - 1)] + [1])
            return last

        return helper(numRows)


if __name__ == '__main__':
    print(Solution().dp(5))
    print(Solution().recursive(5))
