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
            思路：
                1、初始化一个结果集。
                2、循环遍历intervals，如果结果集为空，则将当前元素插入到结果集中。
                3、如果结果集有元素，则取出来和当前元素比较是否可以合并，如果可以合并替换结果集元素的内容，否则将当前元素追加到结果集中。
                4、如果newInterval有值，则将结果集中的做后一个元素取出来和newInterval做比较。
                5、如果newInterval和最后一个元素有交集，则合并。
                6、如果newInterval和最后一个元素没有交集，则判断newInterval是否整体小于最后一个元素，如果小于就插入到最后一个元素前面。否则跳过
                7、如果将newInterval添加到结果集了，就将newInterval置成空。
                8、最后返回时，需要判断是否有newInterval就加intervals追加到res后面，因为如果有说明newInterval很大或者 intervals是空。
                9、整体思路解说
        """
        res = []

        if intervals:

            for start, end in intervals:
                if not res:
                    res.append([start, end])
                else:
                    check_start, check_end = res[-1]
                    if check_start <= start <= check_end:
                        res[-1] = [min(start, check_start), max(end, check_end)]
                    else:
                        res.append([start, end])

                if newInterval:
                    check_start, check_end = res[-1]

                    tmp_start, tmp_end = newInterval

                    if check_start <= tmp_start <= check_end or tmp_start <= check_start <= tmp_end:
                        # TODO 比较一下目标数组 是否在数组中  这里是关键
                        newInterval = []
                        info = [min(tmp_start, check_start), max(tmp_end, check_end)]
                        if res:
                            res[-1] = info
                        else:
                            res.append(info)
                    else:
                        # TODO 可能目标数组远远小于最后一个，这一步也不能少
                        if tmp_end < check_start:
                            # res.insert(-1, [tmp_start, tmp_end])  insert 时间复杂度O(n) append 是O(1)

                            tmp_info = res[-1]
                            res[-1] = [tmp_start, tmp_end]
                            res.append(tmp_info)
                            newInterval = []

        return res + [newInterval] if newInterval else res

# if __name__ == '__main__':
#     print(Solution().insert([[1, 5]], [0, 0]))
