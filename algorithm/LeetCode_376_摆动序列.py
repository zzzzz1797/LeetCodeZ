"""
    如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
    例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，
    第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

    给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

    示例 1:
        输入: [1,7,4,9,2,5]
        输出: 6
        解释: 整个序列均为摆动序列。

    示例 2:
        输入: [1,17,5,10,13,15,10,5,16,8]
        输出: 7
        解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

    示例 3:
        输入: [1,2,3,4,5,6,7,8,9]
        输出: 2
"""

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
            摆动子序列
            当序列有一段连续的递增或者递减的时候，会形成摇摆的子序列，
            我们只需要保留这段连续的子序列的首尾元素，这样更可能使得尾部元素的后一个元素成为摇摆子序列的下一个元素
        """
        return self.solve_1(nums)

    @classmethod
    def dp(cls, nums: List[int]) -> int:
        """
            动态规划
            dp[i][j] 代表第0个数组 到i个数字中的摆动序列的最大长度  j代表最后一个差值是正数还是负数

            当有差值的时候
                差值是负数
                dp[i][0] = max(dp[i-1][1]+1, dp[i-1][0])

                差值是正数
                dp[i][1] = max(dp[i-1][0]+1, dp[i-1][1])
            没有差值的时候
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        """
        res = 0
        if nums:
            size = len(nums)
            dp = [[0, 0] for i in range(size)]
            dp[0][0] = 1
            dp[0][1] = 1

            for i in range(1, size):
                check_val = nums[i] - nums[i - 1]

                if check_val > 0:
                    dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1])
                elif check_val < 0:
                    dp[i][0] = max(dp[i - 1][1] + 1, dp[i - 1][0])
                else:
                    dp[i][0] = dp[i - 1][0]
                    dp[i][1] = dp[i - 1][1]
            res = max(dp[-1][0], dp[-1][1])

        return res

    @classmethod
    def solve_1(cls, nums: List[int]) -> int:
        """贪心算法"""
        res = 0
        if nums:
            size = len(nums)
            res = 1
            state = 0  # 用来表示是否到了转折点

            for i in range(1, size):
                if nums[i] > nums[i - 1] and (state == 0 or state == -1):
                    res += 1
                    state = 1

                if nums[i] < nums[i - 1] and (state == 0 or state == 1):
                    res += 1
                    state = -1

        return res
