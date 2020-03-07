"""
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
    使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。
    示例：

        给定数组 nums = [-1, 0, 1, 2, -1, -4]，
        满足要求的三元组集合为：
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
    https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums.sort()

        for index, row in enumerate(nums):
            if row > 0:
                break

            if index > 0 and nums[index - 1] == row:
                continue

            start = index + 1
            end = len(nums) - 1

            while end > start:
                check_sum = nums[index] + nums[start] + nums[end]

                if check_sum == 0:
                    res.append([nums[index], nums[start], nums[end]])

                    while end > start and nums[start] == nums[start + 1]:
                        start += 1

                    while end > start and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1

                elif check_sum < 0:
                    start += 1
                else:
                    end -= 1
        return res
