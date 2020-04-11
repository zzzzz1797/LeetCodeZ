"""
    给定一个可包含重复数字的序列，返回所有不重复的全排列。
    示例:
        输入: [1,1,2]
        输出:
        [
          [1,1,2],
          [1,2,1],
          [2,1,1]
        ]
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.recursive(nums)

    @classmethod
    def recursive(cls, nums: List[int]) -> List[List[int]]:
        """
            时间复杂度：O(n*n!)
            空间复杂度：O(n*n!)
        """
        res = []
        size = len(nums)

        def helper(index):
            if index == size:
                res.append(nums[:])
                return
            used = {}
            for i in range(index, size):
                check = nums[i]
                if used.get(check):
                    continue

                used[check] = True
                nums[i], nums[index] = nums[index], nums[i]
                helper(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        helper(0)

        return res


if __name__ == '__main__':
    print(Solution.recursive([1, 1, 2]))
