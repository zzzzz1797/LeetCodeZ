"""
    给定一个包含n个整数的数组nums和一个目标值target，判断nums中是否存在四个元素a，b，c和d，使得a+b+c+d的值与target相等？
    找出所有满足条件且不重复的四元组。
    注意：
        答案中不可以包含重复的四元组。
    示例：
        给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
    满足要求的四元组集合为：
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass

    @classmethod
    def solve_1(cls, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        size = len(nums)
        res = []

        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[size - 1] + nums[size - 2] + nums[size - 3] < target:
                continue

            for j in range(i + 1, size - 2):
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[size - 2] + nums[size - 1] < target:
                    continue

                left = j + 1
                right = size - 1

                while left < right:
                    check_target = nums[i] + nums[j] + nums[left] + nums[right]
                    if check_target == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif check_target > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    print(Solution().solve_1([1, 0, -1, 0, -2, 2], 0))
