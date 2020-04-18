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
        return self.iteration(nums)

    @classmethod
    def iteration(cls, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tmp_info = []
            for tmp in res:
                tmp_info.append(tmp + [num])
            res.extend(tmp_info)
        return res

    @classmethod
    def recursive(cls, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)

        def helper(index: int, tmp_res: List[int]):
            if index == size:
                res.append(tmp_res[:])
                return

            helper(index + 1, tmp_res)

            tmp_res.append(nums[index])
            helper(index + 1, tmp_res)
            tmp_res.pop()

        helper(0, [])
        return res

    @classmethod
    def recursive_1(cls, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)

        def helper(index, tmp_res):
            res.append(tmp_res)
            if index == size:
                return

            for i in range(index, size):
                helper(i + 1, tmp_res + [nums[i]])

        helper(0, [])
        return res


if __name__ == '__main__':
    print(Solution().iteration([1, 2, 3]))
    print(Solution().recursive([1, 2, 3]))
    print(Solution().recursive_1([1, 2, 3]))
