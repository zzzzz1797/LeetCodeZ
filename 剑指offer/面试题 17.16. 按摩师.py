""":argument
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动
示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
"""
""":argument
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动
示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
"""
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        return self.solve_1(nums)

    @classmethod
    def solve_1(cls, nums: List[int]) -> int:
        """
            时间复杂度：O(n)
            空间复杂度：O(n)
            状态转移方程：
                dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
                i代表第i个预约
                dp[i] 代表当前预约能的最大时长
        """
        nums_len = len(nums)
        res = 0
        if nums_len:
            dp = [0] * (nums_len + 1)
            dp[1] = nums[0]

            for i in range(2, nums_len + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            res = dp[nums_len]
        return res

    @classmethod
    def solve_2(cls, nums):
        nums_len = len(nums)
        if nums_len:
            first = 0
            second = nums[1]

            for i in range(1, nums_len + 1):
                second, first = max(second, first + nums[i - 1]), second
            return second


if __name__ == "__main__":
    print(Solution().massage([]))
