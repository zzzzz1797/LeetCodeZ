"""
        给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
    一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
    返回一对观光景点能取得的最高分。
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pass

    @classmethod
    def solve_1(cls, A: List[int]) -> int:
        """
            A[i] + A[j] + i - j
            对于景点j来说，A[j]-j是不变的，因此A[i] + i越大，得分越高
        """
        res = 0
        tmp_max = A[0] + 0

        for index, row in enumerate(A):
            if index == 0:
                continue
            res = max(res, tmp_max + row - index)
            tmp_max = max(tmp_max, row + index)
        return res
