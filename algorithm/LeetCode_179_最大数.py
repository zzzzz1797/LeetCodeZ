"""
    给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
    示例 1:
        输入: [10,2]
        输出: 210
    示例 2:
        输入: [3,30,34,5,9]
        输出: 9534330
"""

from typing import List


class Comparators(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return self.solve_1(nums)

    @classmethod
    def solve_1(cls, nums: List[int]) -> str:
        new_nums = sorted(map(str, nums), key=Comparators)
        return res if (res := new_nums) and res[0] != "0" else "0"


if __name__ == '__main__':
    print(Solution.solve_1([0, 0]))
