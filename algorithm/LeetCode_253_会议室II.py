"""
    给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，
    同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

    示例 1:
        输入: [[0, 30],[5, 10],[15, 20]]
        输出: 2

    示例 2:
        输入: [[7,10],[2,4]]
        输出: 1
"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass

    @classmethod
    def solve_1(cls, intervals: List[List[int]]) -> int:
        """
            思路：
                1、按照开始时间对会议进行排序。
                2、初始化一个最小堆，将第一个会议的结束时间加入到堆中，我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
                3、对于每一个房间，检查这个堆顶元素是否空闲。
                    3.1、如果房间空闲，则从堆顶拿出该元素。
                    3.2、更新堆顶元素
                4、处理完成后，堆的大小就是需要的房间数。

        """
        heap = []
        if intervals:
            intervals.sort()
            heapq.heappush(heap, intervals[0][1])
            for i in intervals[1:]:
                if heap[0] <= i[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, i[1])
        return len(heap)


if __name__ == '__main__':
    print(Solution().solve_1([[7, 10], [2, 4]]))
