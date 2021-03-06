"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

    示例:
        输入: [1,2,3]
        输出:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.recursive(nums)

    @classmethod
    def recursive(cls, nums: List[int]) -> List[List[int]]:
        """"
            时间复杂度：应该是O(n!)
        """
        res = []
        size = len(nums)

        def helper(index):
            if index == size:
                res.append(nums[:])

            for i in range(index, size):
                nums[i], nums[index] = nums[index], nums[i]
                helper(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        helper(0)
        return res
