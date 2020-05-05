"""
    给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pass

    @classmethod
    def dp(cls, rowIndex: int) -> List[int]:
        prev = []
        curr = []
        for i in range(rowIndex + 1):
            curr = [1 for i in range(i + 1)]
            for j in range(1, i):
                curr[j] = prev[i - 1] + prev[j]
            prev = curr
        return curr
