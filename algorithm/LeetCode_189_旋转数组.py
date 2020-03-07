"""
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

    示例 1:
        输入: [1,2,3,4,5,6,7] 和 k = 3
        输出: [5,6,7,1,2,3,4]
        解释:
            向右旋转 1 步: [7,1,2,3,4,5,6]
            向右旋转 2 步: [6,7,1,2,3,4,5]
            向右旋转 3 步: [5,6,7,1,2,3,4]

    示例 2:
        输入: [-1,-100,3,99] 和 k = 2
        输出: [3,99,-1,-100]
        解释:
            向右旋转 1 步: [99,-1,-100,3]
            向右旋转 2 步: [3,99,-1,-100]

    说明:
        尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
        要求使用空间复杂度为 O(1) 的 原地 算法。
    https://leetcode-cn.com/problems/rotate-array
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        return self.use_reverse(nums, k)

    @classmethod
    def use_loop(cls, nums: List[int], k: int) -> None:
        nums_len = len(nums)
        k = k % nums_len

        move_times = index = 0

        while index < len(nums):
            value = nums[index]
            new_index = (index + k) % nums_len

            while True:
                old_value = nums[new_index]

                # 更新值
                nums[new_index] = value
                move_times += 1

                new_index = (index + k) % nums_len
                value = old_value

                if new_index == index:
                    move_times += 1
                    nums[new_index] = value
                    break
            index += 1

            if move_times == nums_len:
                break

    @classmethod
    def use_reverse(cls, nums: List[int], k: int) -> None:
        k = k % len(nums)
        cls.reversed_nums(nums, 0, len(nums) - 1)
        cls.reversed_nums(nums, 0, k - 1)
        cls.reversed_nums(nums, k, len(nums) - 1)

    @classmethod
    def reversed_nums(cls, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
