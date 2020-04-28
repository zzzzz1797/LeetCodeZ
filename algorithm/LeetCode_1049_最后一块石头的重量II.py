"""
    有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
        如果 x == y，那么两块石头都会被完全粉碎；
        如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
        最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

    示例：
        输入：[2,7,4,1,8,1]
        输出：1
        解释：
            组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
            组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
            组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
            组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
    提示：
        1 <= stones.length <= 30
        1 <= stones[i] <= 1000
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        pass

    @classmethod
    def solve_1(cls, stones: List[int]) -> int:
        """动态规划"""
        size = len(stones)
        total = sum(stones)

        max_capacity = total // 2
        dp = [0] * (max_capacity + 1)

        print(max_capacity, total)
        for i in range(size):
            cur_stone = stones[i]
            for j in range(max_capacity, cur_stone - 1, -1):
                dp[j] = max(dp[j], dp[j - cur_stone] + cur_stone)
        return total - 2 * dp[max_capacity]

    @classmethod
    def solve_2(cls, stones: List[int]) -> int:
        """
            https://leetcode-cn.com/problems/last-stone-weight-ii/solution/0-1bei-bao-by-yaosw/
            思路：
                假设有四个石头，对应的重量分别是a,b,c,d
                第一次挑出来a,b，然后得到 a-b, c, d
                第二次挑出来a-b、c，得到 c-a+b,d
                第三次挑出来c-a+b、d，得到 d-c+a-b
                所以求的最后一块石头其实是 所有石头加减的结果
                所以可以转化为分成两堆石头 求最小差值的问题， 也就是求一堆石头最接近sum/2的问题
                 dp[i][j]代表选i个石头的最大重量j, 其中容量为sum/2, 即求最大的j<sum/2
        """
        total = sum(stones)
        size = len(stones)

        dp = [[0 for i in range(total // 2 + 1)] for j in range(size + 1)]

        for i in range(1, size + 1):
            for j in range(1, total // 2 + 1):
                if stones[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return total - 2 * dp[-1][-1]


if __name__ == '__main__':
    print(Solution().solve_1([2, 7, 4, 1, 8, 1]))
    print(Solution().solve_1([8, 2, 4, 4, 8]))
