"""
    我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。 （这里，平面上两点之间的距离是欧几里德距离。）
    你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
    示例 1：
        输入：points = [[1,3],[-2,2]], K = 1
        输出：[[-2,2]]
        解释：
        (1, 3) 和原点之间的距离为 sqrt(10)，
        (-2, 2) 和原点之间的距离为 sqrt(8)，
        由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
        我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。

    示例 2：
        输入：points = [[3,3],[5,-1],[-2,4]], K = 2
        输出：[[3,3],[-2,4]]
        （答案 [[-2,4],[3,3]] 也会被接受。）
    提示：
        1 <= K <= points.length <= 10000
        -10000 < points[i][0] < 10000
        -10000 < points[i][1] < 10000
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pass

    @classmethod
    def solve_1(cls, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda i: i[0] * i[0] + i[1] * i[1])
        return points[:K]

    @classmethod
    def solve_2(cls, points: List[List[int]], K: int) -> List[List[int]]:
        size = len(points)
        start = 0
        end = size - 1
        if K == size:
            return points

        while start <= end:
            mid = cls.partition(start, end, points)
            print(mid, "fff")
            if mid == K:
                return points[:mid]
            elif mid < K:
                start = mid + 1
            else:
                end = mid - 1
        return []

    @classmethod
    def partition(cls, start, end, points):
        index = start - 1
        target = points[end]

        for i in range(start, end):
            if cls.compare(target, points[i]) >= 0:
                index += 1
                points[i], points[index] = points[index], points[i]

        points[index + 1], points[end] = points[end], points[index + 1]
        return index + 1

    @classmethod
    def compare(cls, o1, o2) -> int:
        """
            大于返回1
            小于返回-1
            等于返回0
        """
        target1 = o1[0] * o1[0] + o1[1] * o1[1]
        target2 = o2[0] * o2[0] + o2[1] * o2[1]

        if target1 > target2:
            return 1
        elif target1 < target2:
            return -1
        return 0


if __name__ == '__main__':
    # print(Solution().solve_1([[3, 3], [5, -1], [-2, 4]], 2))
    # print(Solution().solve_2([[3, 3], [5, -1], [-2, 4]], 2))
    # print(Solution().solve_1([[1, 3], [-2, 2]], 1))
    # print(Solution().solve_2([[1, 3], [-2, 2]], 1))
    print(Solution().solve_1([[0, 1], [1, 0]], 2))
    print(Solution().solve_2([[0, 1], [1, 0]], 2))
