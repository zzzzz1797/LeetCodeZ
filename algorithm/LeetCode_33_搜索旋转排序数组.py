"""
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。

    你的算法时间复杂度必须是 O(log n) 级别。
    示例 1:
        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4

    示例 2:
        输入: nums = [4,5,6,7,0,1,2], target = 3
        输出: -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass

    @classmethod
    def solve_1(cls, nums: List[int], target: int) -> int:
        """二分查找"""
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid

            if nums[start] > mid_val:
                # 说明后面是有序的
                if mid_val < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                # 说明前面是有序的
                if nums[start] <= target < mid_val:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
