"""
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:
        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

    进阶:
        如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass

    @classmethod
    def greedy(cls, nums: List[int]) -> int:
        """
            贪心算法
            每一步都选则最优方案
        """
        res = cur = 0

        for index, num in enumerate(nums):
            if index == 0:
                res = num
                cur = num
            else:
                cur = max(num, cur + num)
                res = max(res, cur)
        return res

    @classmethod
    def dp_1(cls, nums: List[int]) -> int:
        """
            dp[i] 表示第下标为i时的最大子序和
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        """
        dp = [float("-inf") for i in range(len(nums))]

        for index, num in enumerate(nums):
            if index == 0:
                dp[index] = num
            else:
                dp[index] = max(num, dp[index - 1] + num)
        return max(dp)


if __name__ == '__main__':
    print(Solution.dp_1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
