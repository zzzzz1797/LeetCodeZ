"""
    给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
    给定 n 和 k，返回第 k 个排列。
    说明：
        给定 n 的范围是 [1, 9]。
        给定 k 的范围是[1,  n!]。

    示例 1:
        输入: n = 3, k = 3
        输出: "213"
    示例 2:
        输入: n = 4, k = 9
        输出: "2314"
"""
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pass

    @classmethod
    def solve_1(cls, n: int, k: int):
        info = [str(i) for i in range(1, n + 1)]
        res = ""
        k = k - 1

        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res += info.pop(a)
        return res

    @classmethod
    def solve_2(cls, n: int, k: int):
        """
            参考 https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
        """

        def dfs(k_, index):
            if index == n:
                return
            cnt = factorial[n - index - 1]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k_:
                    k_ -= cnt
                    continue
                res.append(i)
                used[i] = True
                dfs(k_, index + 1)

        factorial = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        used = [False for i in range(n + 1)]

        res = []

        dfs(k, 0)

        return "".join(map(str, res))
