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
        pass

    @classmethod
    def use_double_pointer(cls, nums: List[int]) -> List[List[int]]:
        """
            1，对目标数据 进行排序
            2，每次遍历数组时 过滤值相同的元素
            3，用两个指针从当前元素的下一个位置  和  目标数据的最后一个位置开始遍历
            时间复杂度：O(n^2)
            空间复杂度：O(1)
        """

        # 初始化
        res = []
        nums.sort()

        for index, num in enumerate(nums):
            if num > 0:
                # 因为已经排好序了，所以当出现大于0的元素，则说明这个元素和后面元素之和肯定会大于0
                return res
            if index > 0 and nums[index - 1] == nums[index]:
                # 去重复
                continue

            start_index = index + 1
            end_index = len(nums) - 1
            while start_index < end_index:
                check_sum = nums[index] + nums[start_index] + nums[end_index]
                if check_sum == 0:
                    res.append([nums[index], nums[start_index], nums[end_index]])
                    while start_index < end_index and nums[start_index] == nums[start_index + 1]:
                        # 去重复
                        start_index += 1

                    while start_index < end_index and nums[end_index] == nums[end_index - 1]:
                        # 去重复
                        end_index -= 1
                    start_index += 1
                    end_index -= 1
                elif check_sum > 0:
                    end_index -= 1
                else:
                    start_index += 1
        return res
