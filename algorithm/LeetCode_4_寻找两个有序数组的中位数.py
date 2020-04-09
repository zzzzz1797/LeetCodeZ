"""
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    示例 1:
        nums1 = [1, 3]
        nums2 = [2]
        则中位数是 2.0

    示例 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        则中位数是 (2 + 3)/2 = 2.5
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

    @classmethod
    def solve_2(cls, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        left = (size1 + size2 + 1) // 2
        right = (size1 + size2 + 2) // 2

        def get_k(l1, r1, l2, r2, n1, n2, target):
            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1
            # n1 始终小于n2 如果有数组空肯定是n1
            if len1 > len2:
                return get_k(l2, r2, l1, r1, n2, n1, target)
            if len1 == 0:
                return n2[l2 + target - 1]
            if target == 1:
                return min(nums1[l1], nums2[l2])

            i = l1 + min(len1, target // 2) - 1
            j = l2 + min(len2, target // 2) - 1

            if nums1[i] > nums2[j]:
                return get_k(l1, r1, j + 1, r2, n1, n2, target - (j - l2 + 1))
            return get_k(i + 1, r1, l2, r2, n1, n2, target - (i - l1 + 1))

        res = get_k(0, size1 - 1, 0, size2 - 2, nums1, nums2, left) + get_k(0, size1 - 1, 0, size2 - 2, nums1, nums2,
                                                                            right)
        return res / 2

    @classmethod
    def solve_1(cls, nums1: List[int], nums2: List[int]) -> float:
        """
            时间复杂度：O(m+n)
            空间复杂度：O(1)

            思路：
                1、不管两个数组长度之和是偶数还是奇数，找到中位数的都会走 m+n // 2 + 1次
                2、只不过是每次循环的时候，用两个变量分别保存之前的循环所在值和现在的所在值
                3、如果长度之和是偶数，则中位数是两个变量之和除以2，否则是第二个变量的值。
        """
        size1 = len(nums1)
        size2 = len(nums2)
        total_size = size1 + size2

        left = right = left_index = right_index = 0

        for i in range(total_size // 2 + 1):
            left = right

            if left_index < size1 and (right_index >= size2 or nums2[right_index] > nums1[left_index]):
                right = nums1[left_index]
                left_index += 1
            else:
                right = nums2[right_index]
                right_index += 1

        if total_size % 2 == 0:
            return (left + right) / 2.0
        return right
