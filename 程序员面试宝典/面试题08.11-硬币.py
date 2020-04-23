"""
    硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
    示例1:
        输入: n = 5
        输出：2
        解释: 有两种方式可以凑成总金额:
            5=5
            5=1+1+1+1+1

    示例2:
        输入: n = 10
        输出：4
        解释: 有四种方式可以凑成总金额:
            10=10
            10=5+5
            10=5+1+1+1+1+1
            10=1+1+1+1+1+1+1+1+1+1
"""


class Solution:
    def waysToChange(self, n: int) -> int:
        pass

    @classmethod
    def solve_1(cls, n: int) -> int:
        """
            动态规划 dp
            dp[i][j] 表示 遍历到i这个硬币时组成金额j的方法
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

            dp[i-1][j] 表示这个硬币没有取
            dp[i][j-coins[i]] 表示这个硬币取了
        """
        coins = [1, 5, 10, 25]
        dp = [[0 for j in range(n + 1)] for i in range(4)]

        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(4):
            dp[i][0] = 1

        print(dp)

        for i in range(1, 4):
            for j in range(1, n + 1):
                if j >= coins[i]:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - coins[i]]) % 1000000007
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[3][n]

    @classmethod
    def solve_2(cls, n: int) -> int:
        """
        时间复杂度：O(m*n)
        空间复杂度：O(m)
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        coins = [1, 5, 10, 15]

        for i in range(len(coins)):
            for j in range(1, n + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]
        return dp[n]


if __name__ == '__main__':
    print(Solution().solve_1(4))
