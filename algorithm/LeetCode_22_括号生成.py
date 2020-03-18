"""
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
    例如，给出 n = 3，生成结果为：
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.dp(n)

    @classmethod
    def dfs(cls, n: int) -> List[str]:
        def helper(left_num: int, right_num: int, check_n: int, tmp_str: str, tmp_res: List[str]):
            # terminator 终止条件
            if left_num == right_num == check_n:
                tmp_res.append(tmp_str)
                return

            # process
            if left_num < check_n:
                # drill down  说明左括号还不够
                helper(left_num + 1, right_num, check_n, tmp_str + "(", tmp_res)

            # process
            if right_num < left_num:
                # drill down 说明右括号还不够
                helper(left_num, right_num + 1, check_n, tmp_str + ")", tmp_res)

        res = []

        helper(0, 0, n, "", res)

        return res

    @classmethod
    def dp(cls, n: int) -> List[str]:
        """
            动态规划
            dp数组 dp[i] 表示 使用i对括号能生成的组合

            dp[i] = "(" + dp[j]  + ")" + dp[i-j-1]   j = 0, 1, ..., i - 1
        """
        res = []

        if n:
            dp = [[] for i in range(n + 1)]
            dp[0] = [""]

            for i in range(1, n + 1):
                cur = []
                for j in range(i):
                    left = dp[j]
                    right = dp[i - j - 1]
                    for s1 in left:
                        for s2 in right:
                            cur.append("(" + s1 + ")" + s2)
                dp[i] = cur
            res = dp[n]
        return res
