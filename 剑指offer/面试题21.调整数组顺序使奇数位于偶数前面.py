"""
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
    示例：
        输入：nums = [1,2,3,4]
        输出：[1,3,2,4]
        注：[3,1,2,4] 也是正确的答案之一。
"""

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1

        while start < end:
            while start < end and nums[start] % 2 != 0:
                start += 1

            while start < end and nums[end] % 2 == 0:
                end -= 1

            nums[start], nums[end] = nums[end], nums[start]
        return nums
