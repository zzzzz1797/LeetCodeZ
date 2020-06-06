"""
    给定一个未排序的整数数组，找出最长连续序列的长度。
    示例:
        输入: [100, 4, 200, 1, 3, 2]
        输出: 4
        解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass

    @classmethod
    def solve_1(cls, nums: List[int]):
        res = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                # 说明这个数现在是起点, 那就以这个数为起点开始查找最长连续子序列
                curr_num = num
                curr_res = 1

                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_res += 1
                res = max(curr_res, res)
        return res
