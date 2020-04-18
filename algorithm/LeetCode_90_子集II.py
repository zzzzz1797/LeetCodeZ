"""
    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    示例:
        输入: [1,2,2]
        输出:
        [
          [2],
          [1],
          [1,2,2],
          [2,2],
          [1,2],
          []
        ]
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.recursive(nums)

    @classmethod
    def recursive(cls, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)
        nums.sort()

        def helper(index, tmp_res):
            res.append(tmp_res)
            if index == size:
                return
            for i in range(index, size):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                helper(i + 1, tmp_res + [nums[i]])

        helper(0, [])
        return res


if __name__ == '__main__':
    print(Solution().recursive([1, 2, 2]))
