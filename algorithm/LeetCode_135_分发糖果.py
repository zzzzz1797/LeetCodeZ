"""
    老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
    你需要按照以下要求，帮助老师给这些孩子分发糖果：
        每个孩子至少分配到 1 个糖果。
        相邻的孩子中，评分高的孩子必须获得更多的糖果。
        那么这样下来，老师至少需要准备多少颗糖果呢？

    示例 1:
        输入: [1,0,2]
        输出: 5
        解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

    示例 2:
        输入: [1,2,2]
        输出: 4
        解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
             第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        pass

    @classmethod
    def dp(cls, ratings: List[int]) -> int:
        """
            动态规划
            dp[i] 代表第i个孩子应该分到的糖果
            只要直到dp[i+1] 和 dp[i-1] 就可以知道dp[i]的值了
            相邻的孩子中，评分高 且站在右边 的孩子必须获得更多的糖果。
            相邻的孩子中，评分高 且站在左边 的孩子必须获得更多的糖果。
        """
        size = len(ratings)
        dp = [1 for i in range(size)]

        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1

        for j in range(size - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                dp[j] = max(dp[j], dp[j + 1] + 1)
        return sum(dp)

    @classmethod
    def solve_1(cls, ratings: List[int]) -> int:
        """https://leetcode-cn.com/problems/candy/solution/bo-feng-bo-gu-yi-ci-bian-li-rong-yi-xiang-dao-dan-/"""
        size = len(ratings)
        index = cnt = total = 0

        while index < size:
            j = index + 1
            # 确定波峰
            while j < size and ratings[j] > ratings[j - 1]:
                j += 1

            mid = j
            up = j - index

            # 确定    波谷
            while j < size and ratings[j] < ratings[j - 1]:
                j += 1

            down = j - mid + 1

            if up < down:
                up, down = down, up

            total += up * (up + 1) // 2 + down * (down - 1) // 2

            if j == index + 1:
                index = index + 1
            else:
                index = j - 1
                cnt += 1
        return total - cnt
