"""
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    示例 1:
        输入: [3,2,1,5,6,4] 和 k = 2
        输出: 5

    示例 2:
        输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
        输出: 4

    说明:
        你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.solve_1(nums, k)

    @classmethod
    def solve_1(cls, nums: List[int], k: int) -> int:
        """
            快速选择 转换为求第nums-k小元素，使用快排的思想
        """

        def partition(l, h, n):
            index = l - 1
            target = n[h]

            for i in range(l, h):
                if n[i] <= target:
                    index += 1
                    n[index], n[i] = n[i], n[index]
            n[index + 1], n[h] = n[h], n[index + 1]
            return index + 1

        num_size = len(nums)
        start = 0
        end = num_size - 1
        target_index = num_size - k
        while start <= end:
            index = partition(start, end, nums)
            if index == target_index:
                return nums[index]
            elif index < target_index:
                start += 1
            else:
                end -= 1
        return -1
