"""
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

    示例:
        输入:
            nums = [1,2,3]
        输出:
            [
              [3],
              [1],
              [2],
              [1,2,3],
              [1,3],
              [2,3],
              [1,2],
              []
            ]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums:
            # self.DFS(res, nums, [], 0)
            self.iteration(res, nums)
        return res

    @classmethod
    def iteration(cls, res: List[List[int]], nums: List):
        res.append([])
        for num in nums:
            res.extend([tmp + [num] for tmp in res])

    @classmethod
    def DFS(cls, res: List[List[int]], nums: List[int], tmp_res: List[int], index: int):
        # terminator
        if index == len(nums):
            res.append(tmp_res[:])
            return

        # process
        # 不选这个数
        cls.DFS(res, nums, tmp_res, index + 1)

        # 选这个数
        tmp_res.append(nums[index])
        cls.DFS(res, nums, tmp_res, index + 1)

        # reverse state
        tmp_res.pop()
