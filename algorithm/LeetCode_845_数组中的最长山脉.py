"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
    B.length >= 3
    存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。
如果不含有 “山脉” 则返回 0。

示例 1：
    输入：[2,1,4,7,3,2,5]
    输出：5
    解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。

示例 2：
    输入：[2,2,2]
    输出：0
    解释：不含 “山脉”。
 
提示：
    0 <= A.length <= 10000
    0 <= A[i] <= 10000
"""
from enum import Enum
from typing import List


class MountainPosition(Enum):
    DOWN = -1
    AVERAGE = 0
    UP = 1


class Solution:
    """
        三种状态：
            上
            下
            平
        最大距离的 = 上的起点 + 下的终点 + 1

    """

    def longestMountain(self, A: List[int]) -> int:
        return self.solve_1(A)

    @classmethod
    def solve_1(cls, mountains: List[int]) -> int:
        max_mountain_length = 0
        cur_mountain_length = 0
        mountain_length = len(mountains)
        last_mountain_position = MountainPosition.AVERAGE

        for index in range(1, mountain_length):
            if mountains[index - 1] < mountains[index]:
                # 上
                if last_mountain_position == MountainPosition.UP:
                    # 如果之前的状态是上，则说明山脉的高度还在增加
                    cur_mountain_length += 1
                else:
                    # 如果之前的状态是下，则说明生成了一个新的山脉
                    max_mountain_length = max(max_mountain_length, cur_mountain_length)
                    last_mountain_position = MountainPosition.UP
                    cur_mountain_length = 2  # index - (index-1) + 1 = 2
            elif mountains[index - 1] > mountains[index]:
                if last_mountain_position == MountainPosition.DOWN:
                    cur_mountain_length += 1
                elif last_mountain_position == MountainPosition.UP:
                    # 说明开始下了，需要找到下的终点
                    last_mountain_position = MountainPosition.DOWN
                    cur_mountain_length += 1
            else:
                if last_mountain_position == MountainPosition.DOWN:
                    max_mountain_length = max(max_mountain_length, cur_mountain_length)
                last_mountain_position = MountainPosition.AVERAGE
                cur_mountain_length = 0

        if last_mountain_position == MountainPosition.DOWN and max_mountain_length < cur_mountain_length:
            max_mountain_length = cur_mountain_length

        return max_mountain_length

    @classmethod
    def solve_2(cls, mountains):
        mountain_length = len(mountains)
        max_mountain_length = 0
        left_mountains = [0] * mountain_length
        right_mountains = [0] * mountain_length

        # 从右往左遍历
        for index in range(mountain_length - 2, -1, -1):
            if mountains[index] > mountains[index + 1]:
                right_mountains[index] = right_mountains[index + 1] + 1

        # 从左往右遍历
        for index in range(1, mountain_length):
            if mountains[index] > mountains[index - 1]:
                left_mountains[index] = left_mountains[index - 1] + 1

        # 计算出最大的长度
        for index in range(mountain_length):
            if left_mountains[index] > 0 and right_mountains[index] > 0:
                # 说明这个点处于山峰的位置
                max_mountain_length = max(max_mountain_length, left_mountains[index] + right_mountains[index] + 1)
        return max_mountain_length


if __name__ == "__main__":
    print(Solution().solve_2([2,1,4,7,3,2,5]))
