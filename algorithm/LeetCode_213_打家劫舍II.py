"""
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
    这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
    同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

    示例 1:
        输入: [2,3,2]
        输出: 3
        解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

    示例 2:
        输入: [1,2,3,1]
        输出: 4
        解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
             偷窃到的最高金额 = 1 + 3 = 4 。
"""
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            这道题其实和打家劫舍1(https://leetcode-cn.com/problems/house-robber/)一样的思路，
            只不过是首位两家是相邻的，构成了一个环状的结构。
            所以我们可以计算两次
                第一次计算 包括第一家但是不包括最后一家能偷到的最大金额，记为A1
                第二次计算 包括最后一家但是不包括第一家能偷到的最大金额，记为A2
            我们能偷到的最大金额就是Max(A1, A2)
            这里只实现一下递归的写法。剩下的和打家劫舍都一样
        """
        if len(nums) == 1:
            return nums[0]

        return max(self.recursive(nums[:len(nums) - 1]), self.recursive(nums[1:]))

    @classmethod
    def recursive(cls, nums: List[int]) -> int:
        nums_len = len(nums)

        @lru_cache(None)
        def helper(index):
            # terminator
            if index == nums_len - 1:
                return nums[index]

            if index >= nums_len:
                return 0

            # process

            # drill down
            choose_index = helper(index + 2) + nums[index]

            not_choose_index = helper(index + 1)

            return max(choose_index, not_choose_index)

            # reverse state

        res = 0
        if nums:
            res = helper(0) if nums_len > 1 else nums[0]
        return res
