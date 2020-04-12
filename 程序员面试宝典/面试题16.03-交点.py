"""
    给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
    要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。

    示例 1：
        输入：
        line1 = {0, 0}, {1, 0}
        line2 = {1, 1}, {0, -1}
        输出： {0.5, 0}

    示例 2：
        输入：
        line1 = {0, 0}, {3, 3}
        line2 = {1, 1}, {2, 2}
        输出： {1, 1}

    示例 3：
        输入：
        line1 = {0, 0}, {1, 1}
        line2 = {1, 0}, {2, 1}
        输出： {}，两条线段没有交点
    提示：

    坐标绝对值不会超过 2^7
    输入的坐标均是有效的二维坐标
"""
from typing import List


class Solution:
    """
        复制这位老哥的 https://leetcode-cn.com/problems/intersection-lcci/solution/wo-jue-de-wo-yi-jing-hen-nu-li-liao-ke-yi-jiao-zhu/

    """
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        det = lambda a, b, c, d: a * d - b * c

        d = det(x1 - x2, x4 - x3, y1 - y2, y4 - y3)
        p = det(x4 - x2, x4 - x3, y4 - y2, y4 - y3)
        q = det(x1 - x2, x4 - x2, y1 - y2, y4 - y2)

        if d != 0:
            lam, eta = p / d, q / d
            if not (0 <= lam < 1 and 0 <= eta <= 1):
                return []

            return [lam * x1 + (1 - lam) * x2, lam * y1 + (1 - lam) * y2]

        if p != 0 or q != 0:
            return []

        t1, t2 = sorted([start1, end1, ]), sorted([start2, end2])
        if t1[1] < t2[0] or t2[1] < t1[0]:
            return []
        return max(t1[0], t2[0])
