"""
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。

    示例 1:
        输入: [2,3,1,1,4]
        输出: true
        解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
    示例 2:
        输入: [3,2,1,0,4]
        输出: false
        解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass

    @classmethod
    def greedy(cls, nums: List[int]) -> bool:
        """
            1、定义一个max_index, 循环遍历nums
            2、当循环开始时将下标为0对应value复给max_index
            3、当循环不为0时，判断当前index是否大于max_index
            4、如果大于max_index,则说明后面肯定也到达不了，直接返回false
            5、如果可以到达，则需要判断是否要更新max_index
            6、更新的步骤是取当前index+nums[index] 和max_index两者的最大值，然后更新给max_index
            7、循环3 4 5 6 直到整个循环结束，返回True
        """
        max_index = 0
        for index, num in enumerate(nums):
            if index == 0:
                max_index = num
            else:
                if max_index < index:
                    return False
                max_index = max(max_index, num + index)

        return True

    @classmethod
    def dp(cls, nums: List[int]) -> bool:
        """
            如果跳不到i点，那么一定跳不到i后面的点。
            如果可以跳到i点，则说明一定可以跳到i前面的任意一点。

        """
        for i in range(1, len(nums)):
            # 假设跳不到
            flag = False

            # 从后往前开始遍历
            for j in range(i - 1, -1, -1):
                if nums[j] + j >= i:
                    # 如果你能跳到，则之后的点肯定也能跳到
                    flag = True
                    break
            if not flag:
                return False
        return True
