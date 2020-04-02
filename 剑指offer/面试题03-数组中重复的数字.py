"""
    找出数组中重复的数字。
    在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
    请找出数组中任意一个重复的数字。

    示例 1：
        输入：
        [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3
"""

from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        pass

    @classmethod
    def use_sort(cls, nums: List[int]) -> int:
        nums.sort()

        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                return nums[index]

    @classmethod
    def use_mapping(cls, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
            if mapping[num] > 1:
                return mapping[num]

    @classmethod
    def use_iteration(cls, nums: List[int]) -> int:
        for index in range(len(nums)):
            while index != nums[index]:
                if nums[nums[index]] == nums[index]:
                    return nums[index]
                nums[nums[index]], nums[index] = nums[index], nums[nums[index]]


if __name__ == '__main__':
    print(Solution.use_iteration([2, 3, 1, 0, 2, 5, 3]))
