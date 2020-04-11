"""
    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

    示例 1：
        输入：K = 1, N = 2
        输出：2
        解释：
        鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
        否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
        如果它没碎，那么我们肯定知道 F = 2 。
        因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

    示例 2：
        输入：K = 2, N = 6
        输出：3

    示例 3：
        输入：K = 3, N = 14
        输出：4
 
    1 <= K <= 100
    1 <= N <= 10000
"""
from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """
            k 表示鸡蛋的个数
            n 表示楼的层数
        """

        return self.recursive(K, N)

    @classmethod
    @lru_cache(None)
    def recursive_and_mid_search(cls, K: int, N: int) -> int:
        if K == 1 or N == 0:
            return N

        key = (K, N)

        res = float("inf")
        lo = 1
        hi = N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = cls.recursive_and_mid_search(K - 1, mid - 1)  # 蛋碎了
            not_broken = cls.recursive_and_mid_search(K, N - mid)  # 蛋没碎
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)
        return res

    @classmethod
    @lru_cache(None)
    def recursive(cls, K: int, N: int) -> int:
        # terminator
        if K == 1:
            # 这个时候只能一层一层的去试
            return N
        if N == 0:
            # 楼层为0了， 则不需要扔鸡蛋了
            return 0

        # process
        res = float("inf")
        for i in range(1, N + 1):
            res = min(
                res,
                max(
                    cls.recursive(K - 1, i - 1, ),  # 在第i楼扔了一次，鸡蛋碎了
                    cls.recursive(K, N - i)  # 在第i楼扔了一次，鸡蛋碎
                ) + 1  # +1 表示在第i楼扔过了
            )
        return res
