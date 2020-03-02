"""
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

    示例 1:
        给定数组 nums = [1,1,2],
        函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
        你不需要考虑数组中超出新长度后面的元素。

    示例 2:
        给定 nums = [0,0,1,1,1,2,2,3,3,4],
        函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
        你不需要考虑数组中超出新长度后面的元素。
        https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        move_index = 1

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[move_index] = nums[index]
                move_index += 1
        nums[:] = nums[:move_index]
        return move_index


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = Solution().removeDuplicates(nums)
    print(res, nums)
