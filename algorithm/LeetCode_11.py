"""
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    说明：你不能倾斜容器，且 n 的值至少为 2。

    示例:
        输入: [1,8,6,2,5,4,8,3,7]
        输出: 49
    https://leetcode-cn.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left_index = 0
        right_index = len(height) - 1

        while right_index > left_index:
            right_val = height[right_index]
            left_val = height[left_index]

            width = min(left_val, right_val)
            length = right_index - left_index

            tmp_res = width * length
            res = max(res, tmp_res)

            if left_val > right_val:
                right_index -= 1
            else:
                left_index += 1

        return res
