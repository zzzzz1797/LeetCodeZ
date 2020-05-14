"""
    给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax^2 + bx + c，请将函数值产生的数组返回。
    要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。

    示例 1：

        输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
        输出: [3,9,15,33]

    示例 2：
        输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
        输出: [-23,-5,1,7]
"""
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        pass

    @classmethod
    def solve_1(cls, nums: List[int], a: int, b: int, c: int):
        """

            a > 0的话，那从两边往中间，计算结果越来越小。取左右指针，比大小，依次从后往前填到结果即可。
            a < 0的话，那从两边往中间，计算结果必然越来越大。同样取左右指针，比大小，依次从前往后填到结果中即可
            a == 0, 随便塞到上面哪种情况下即可。
        """
        size = len(nums)
        result = [0] * size

        left = 0
        right = size - 1

        if a > 0:
            point, offset = size - 1, -1
        else:
            point, offset = 0, 1

        left_val = cls.calculate(nums[left], a, b, c)
        right_val = cls.calculate(nums[right], a, b, c)

        while left < right:
            if (a <= 0 and left_val < right_val) or (a > 0 and left_val > right_val):
                result[point] = left_val
                left += 1
                left_val = cls.calculate(nums[left], a, b, c)
            else:
                result[point] = right_val
                right -= 1
                right_val = cls.calculate(nums[right], a, b, c)
            point += offset
        result[point] = left_val
        return result

    @classmethod
    def calculate(cls, x, a, b, c):
        return a * x * x + b * x + c
