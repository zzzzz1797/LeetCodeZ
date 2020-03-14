"""
    给定一个无序的整数数组，找到其中最长上升子序列的长度。

    示例:
        输入: [10,9,2,5,3,7,101,18]
        输出: 4
        解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

    说明:

        可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
        你算法的时间复杂度应该为 O(n2) 。
    进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.dp_2(nums)

    @classmethod
    def dp_1(cls, nums: List[int]) -> int:
        """
        dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度
        状态转移方程
        dp[i] = max(dp[i], di[j]+1) for j in range(i)
        时间复杂度：O(n**2)
        空间复杂度：O(n)
        """
        nums_len = len(nums)
        res = 0
        if nums:
            dp = nums_len * [1]  # 初始化每个元素值为1 代表假设只有当前元素满足上升子序列
            for i in range(1, nums_len):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            res = max(dp)
        return res

    @classmethod
    def dp_2(cls, nums: List[int]) -> int:
        """
            时间复杂度：O(nlogn)
            空间复杂度：O(n)
        """
        res = 0
        if nums:
            nums_len = len(nums)
            tail = [0] * nums_len

            for num in nums:
                i = 0
                j = res

                while i < j:
                    m = (i + j) // 2
                    if tail[m] < num:
                        i = m + 1
                    else:
                        j = m
                tail[i] = num
                if j == res:
                    res += 1
        return res