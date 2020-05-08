"""
    给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    示例 1:
        输入: nums = [-1,0,3,5,9,12], target = 9
        输出: 4
        解释: 9 出现在 nums 中并且下标为 4
    示例 2:
        输入: nums = [-1,0,3,5,9,12], target = 2
        输出: -1
        解释: 2 不存在 nums 中因此返回 -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    @classmethod
    def solve_1(cls, nums: List[int], target: int):
        """
        找到第一个出现的target
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return start if nums[start] == target else -1

    @classmethod
    def solve_2(cls, nums: List[int], target: int):
        """
            找到最后出现的target
        """
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return start - 1 if nums[start - 1] == target else -1


if __name__ == '__main__':
    print(Solution.solve_1([-1, 0, 3, 5, 9, 9, 9, 9, 9, 12], 19))
    print(Solution.solve_2([-1, 0, 3, 5, 9, 9, 9, 9, 9, 12], 9))
