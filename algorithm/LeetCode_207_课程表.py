"""
    你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
    给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

    示例 1:
        输入: 2, [[1,0]]
        输出: true
        解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

    示例 2:
        输入: 2, [[1,0],[0,1]]
        输出: false
        解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 
    提示：
        输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
        你可以假定输入的先决条件中没有重复的边。
        1 <= numCourses <= 10^5
"""
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

    @classmethod
    def solve_1(cls, num_courses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()

        # 定义入度边的数量
        in_degrees = [0 for i in range(num_courses)]
        # 定义节点的下驱节点列表
        sources = [[] for i in range(num_courses)]

        # 初始化变量内容
        for cur, pre in prerequisites:
            in_degrees[cur] += 1
            sources[pre].append(cur)

        # 找到入读边数量为0的节点
        for i in range(len(in_degrees)):
            if not in_degrees[i]:
                queue.append(i)

        # 遍历整个queue
        while queue:
            pre = queue.popleft()
            num_courses -= 1
            for cur in sources[pre]:
                in_degrees[cur] -= 1
                if not in_degrees[cur]:
                    queue.append(cur)
        return num_courses == 0
