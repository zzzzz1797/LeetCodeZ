"""
    给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
    你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

    示例 1:
        输入: [1, 2, 2, 3, 1]
        输出: 2
        解释:
            输入数组的度是2，因为元素1和2的出现频数最大，均为2.
            连续子数组里面拥有相同度的有如下所示:
            [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
            最短连续子数组[2, 2]的长度为2，所以返回2.

    示例 2:
        输入: [1,2,2,3,1,4,2]
        输出: 6
"""

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        pass

    @classmethod
    def solve_1(cls, nums: List[int]) -> int:
        mapping = {}

        # 1. 获取这些元素 以及元素出现的下标
        for index, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = [index]
            else:
                mapping[num].append(index)

        # 2. 找到出现次数最多的那个元素对应的长度
        max_len = 0
        for key, val in mapping.items():
            max_len = max(max_len, len(val))

        # 3. 划分出出现次数最多的元素
        most_elements = []
        for key, val in mapping.items():
            if len(val) == max_len:
                most_elements.append(val)

        # 4. 遍历most_elements，获取最短的子序列
        res = float("inf")
        for elements_index in most_elements:
            res = min(res, elements_index[-1] - elements_index[0] + 1)
        return res


if __name__ == '__main__':
    print(Solution.solve_1([1, 2, 2, 3, 1, 4, 2]))
    print(Solution.solve_1([1, 2, 2, 3, 1]))
