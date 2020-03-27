"""
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。

    如果数组中不存在目标值，返回 [-1, -1]。

    示例 1:
        输入: nums = [5,7,7,8,8,10], target = 8
        输出: [3,4]

    示例 2:
        输入: nums = [5,7,7,8,8,10], target = 6
        输出: [-1,-1]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            时间复杂度：O(logn)
            空间复杂度：O(1)
        """
        res = [-1, -1]
        nums_len = len(nums)

        # 1. 先通过二分查找 其中的一个target
        target_index = self.mid_query(nums, 0, nums_len - 1, target)
        if target_index == -1:
            return res

        left_res = right_res = target_index

        # 2. 对左边[0, target-1]做二分查找
        end_index = target_index
        while True:
            if 0 <= end_index - 1 < target_index:
                end_index = self.mid_query(nums, 0, end_index - 1, target)
                if end_index != -1:
                    left_res = end_index
                else:
                    break
            else:
                break

        # 3. 对于右边[target+1, nums_len]做二分查找
        start_index = target_index
        while True:
            if target_index < start_index + 1 < nums_len:
                start_index = self.mid_query(nums, start_index + 1, nums_len - 1, target)
                if start_index != -1:
                    right_res = start_index
                else:
                    break
            else:
                break

        return [left_res, right_res]

    @classmethod
    def mid_query(cls, nums: List[int], start, end, target):

        while start <= end:
            mid = (start + end) >> 1  # 等于 //2

            check_num = nums[mid]
            if check_num > target:
                end = mid - 1
            elif check_num < target:
                start = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    print(Solution().searchRange([2, 2], 2))
