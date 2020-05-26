"""
    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

    示例：
        输入：A = [4,5,0,-2,-3,1], K = 5
        输出：7
        解释：
            有 7 个子数组满足其元素之和可被 K = 5 整除：
            [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pass

    @classmethod
    def solve_1(cls, A: List[int], K: int):
        mapping = {0: 1}
        total = 0

        for num in A:
            total += num
            mod = total % K
            mapping[mod] = mapping.get(mod, 0) + 1

        res = 0
        for key, val in mapping.items():
            res += val * (val - 1) // 2
        return res

    @classmethod
    def solve_2(cls, A: List[int], K: int):
        total = res = 0
        mapping = {0: 1}

        for num in A:
            total += num
            mod = total % K
            cnt = mapping.get(mod, 0)
            res += cnt
            mapping[mod] = mapping.get(mod, 0) + 1
        return res
