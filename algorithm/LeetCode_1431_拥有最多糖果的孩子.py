"""
    给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。
    对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。
    注意，允许有多个孩子同时拥有 最多 的糖果数目
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        pass

    @classmethod
    def solve_1(cls, candies: List[int], extraCandies: int) -> List[bool]:
        size = len(candies)
        max_candy = max(candies)
        res = [False for i in range(size)]

        for index, candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                res[index] = True
        return res
