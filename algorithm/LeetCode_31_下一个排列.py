"""
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须原地修改，只允许使用额外常数空间。

    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        思路
            先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
            再找出另一个最大索引 l 满足 nums[l] > nums[k]；
            交换 nums[l] 和 nums[k]；
            最后翻转 nums[k+1:]。
        """
        first_index = -1
        size = len(nums)

        def reverse(n, i, j):
            while i < j:
                n[i], n[j] = n[j], n[i]
                i += 1
                j -= 1

        for index in range(size - 2, -1, -1):
            if nums[index] < nums[index + 1]:
                first_index = index
                break

        if first_index == -1:
            reverse(nums, 0, size - 1)
            return

        second_index = -1

        for index in range(size - 1, first_index, -1):
            if nums[index] > nums[first_index]:
                second_index = index
                break
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        reverse(nums, first_index + 1, size - 1)

