"""
    给出一个区间的集合，请合并所有重叠的区间。

    示例 1:
        输入: [[1,3],[2,6],[8,10],[15,18]]
        输出: [[1,6],[8,10],[15,18]]
        解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

    示例 2:
        输入: [[1,4],[4,5]]
        输出: [[1,5]]
        解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
             时间复杂度：O(nlogn)
             空间复杂度：O(n)

        """
        res = []
        if intervals:
            # 先排序
            intervals.sort(key=lambda i: i[0])

            # 合并
            res = [intervals[0]]

            for data in intervals[1:]:
                start, end = data
                check_start, check_end = res[-1]

                if check_start <= start <= check_end:
                    res[-1] = [check_start, max(end, check_end)]
                else:
                    res.append([start, end])
        return res


if __name__ == '__main__':
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
