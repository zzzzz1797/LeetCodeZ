"""
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        res = float("-inf")
        for index, num in enumerate(nums):
            left = index + 1
            right = size - 1

            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum == target:
                    return target
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum
                if curr_sum - target < 0:
                    left += 1
                else:
                    right -= 1
        return res
