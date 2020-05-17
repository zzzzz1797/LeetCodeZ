"""
    给定两个数组，编写一个函数来计算它们的交集。
    示例 1:
        输入: nums1 = [1,2,2,1], nums2 = [2,2]
        输出: [2]
    示例 2:
        输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        输出: [9,4]
    说明:
        输出结果中的每个元素一定是唯一的。
        我们可以不考虑输出结果的顺序。
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass

    @classmethod
    def solve_1(cls, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for num1 in nums1:
            if num1 not in mapping:
                mapping[num1] = 1

        res = []
        for num2 in nums2:
            if mapping.get(num2):
                mapping[num2] -= 1
                res.append(num2)
        return res


if __name__ == '__main__':
    print(Solution().solve_1([1, 2, 2, 1], [2, 2]))
