"""
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

    示例:
        输入: [0,1,0,2,1,0,1,3,2,1,2,1]
        输出: 6
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        pass

    @classmethod
    def directly(cls, height: List[int]) -> int:
        """
            暴力求解法
            针对于每根柱子 找到左边最高的柱子，然后在找到右边最高的柱子， 如果这两个柱子中的最小值 比当前柱子要大，
        """
        res = 0
        height_len = len(height)

        for index in range(height_len):
            max_left = max_right = 0

            # 找左边最大的柱子
            for left_index in range(0, index):
                max_left = max(max_left, height[left_index])
            # 找右边最大的柱子
            for right_index in range(index + 1, height_len - 1):
                max_right = max(max_right, height[right_index])

            if min(max_left, max_right) > height[index]:
                res += min(max_left, max_right) - height[index]
        return res

    @classmethod
    def dp(cls, height: List[int]) -> int:
        res = 0
        if len(height) >= 3:
            size = len(height)

            max_left_list = [0] * size
            max_right_list = [0] * size
            max_left_list[0] = height[0]
            max_right_list[-1] = height[-1]

            for i in range(1, size):
                max_left_list[i] = max(max_left_list[i - 1], height[i])

            for j in range(size - 2, -1, -1):
                max_right_list[j] = max(max_right_list[j + 1], height[j])

            for c in range(1, size - 1):
                target = min(max_right_list[c], max_left_list[c]) - height[c]
                res += 0 if target <= 0 else target

        return res

    @classmethod
    def double_pointer(cls, height: List):
        res = 0
        if height:
            height_nums = len(height)

            left_index = 0
            right_index = height_nums

            left_max = height[0]
            right_max = height[-1]

            while left_index < right_index:
                left_max = max(left_max, height[left_index])
                right_max = max(right_max, height[right_index])

                if left_max < right_max:
                    res += left_max - height[left_index]
                    left_index += 1
                else:
                    res += right_max - height[right_index]
                    right_index -= 1

        return res


if __name__ == '__main__':
    print(Solution().dp([4, 3, 1, 0, 1, 2, 4]))
