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
        """
            保证剔除的数总是在第k小数的左边
        """
        size1 = len(nums1)
        size2 = len(nums2)

        left = (size1 + size2 + 1) // 2
        right = (size1 + size2 + 2) // 2

        res = cls.get_k(0, size1 - 1, 0, size2 - 1, nums1, nums2, left) + cls.get_k(0, size1 - 1, 0, size2 - 1, nums1,
                                                                                    nums2, right)
        return res / 2

    @classmethod
    def get_k(cls, left1, right1, left2, right2, nums1, nums2, target):
        len1 = right1 - left1 + 1
        len2 = right2 - left2 + 1

        # 始终保持nums2列表里面有值，即有一个空数组也是nums1
        if len1 > len2:
            return cls.get_k(left2, right2, left1, right1, nums2, nums1, target)

        if len1 == 0:
            return nums2[left2 + target - 1]

        if target == 1:
            return min(nums1[left1], nums2[left2])

        i = left1 + min(len1, target // 2) - 1
        j = left2 + min(len2, target // 2) - 1

        if nums1[i] > nums2[j]:
            return cls.get_k(left1, right1, j + 1, right2, nums1, nums2, target - (j - left2 + 1))

        return cls.get_k(i + 1, right1, left2, right2, nums1, nums2, target - (i - left1 + 1))

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

    @classmethod
    def solve_3(cls, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)

        if size1 > size2:
            return cls.solve_3(nums2, nums1)

        k = (size1 + size2 + 1) // 2
        left = 0
        right = size1

        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1
        left_val = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (size1 + size2) % 2 == 1:
            return left_val
        right_val = min(nums1[m1] if m1 < size1 else float("inf"), nums2[m2] if m2 < size2 else float("inf"))
        return (left_val + right_val) / 2


if __name__ == '__main__':
    print(Solution.solve_3([2, 4, 6, 8], [1, 3, 5, 7, 9]))
