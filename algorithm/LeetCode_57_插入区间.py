"""
    给出一个无重叠的 ，按照区间起始端点排序的区间列表。
    在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

    示例 1:
        输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
        输出: [[1,5],[6,9]]

    示例 2:
        输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        输出: [[1,2],[3,10],[12,16]]
        解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            时间复杂度：O(n)
            空间复杂度：O(n)
        """
        res = []

        if intervals:

            for start, end in intervals:
                if not res:
                    res.append([start, end])

                check_start, check_end = res[-1]

                if check_start <= start <= check_end:
                    res[-1] = [min(start, check_start), max(end, check_end)]
                else:
                    res.append([start, end])

                if newInterval:
                    check_start, check_end = res[-1]

                    tmp_start, tmp_end = newInterval

                    if check_start <= tmp_start <= check_end or tmp_start <= check_start <= tmp_end:
                        # 比较一下目标数组 是否在数组中
                        newInterval = []
                        info = [min(tmp_start, check_start), max(tmp_end, check_end)]
                        if res:
                            res[-1] = info
                        else:
                            res.append(info)
                    else:
                        # 可能目标数组远远小于最后一个
                        if tmp_end < check_start:
                            res.insert(-1, [tmp_start, tmp_end])
                            newInterval = []

        return res + [newInterval] if newInterval else res


# if __name__ == '__main__':
#     print(Solution().insert([[1, 5]], [0, 0]))
