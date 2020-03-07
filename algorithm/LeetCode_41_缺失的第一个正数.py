"""
    给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

    示例 1:
        输入: [1,2,0]
        输出: 3

    示例 2:
        输入: [3,4,-1,1]
        输出: 2

    示例 3:
        输入: [7,8,9,11,12]
        输出: 1

    说明:
        你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return self.solve_1(nums)

    @classmethod
    def solve_1(cls, nums: List[int]) -> int:
        """
            索引从0开始，找到 index != nums[index+1]
        """
        nums_len = len(nums)

        for index in range(nums_len):
            while 1 <= nums[index] <= nums_len and nums[index] != nums[nums[index] - 1]:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]

        for i in range(nums_len):
            if i + 1 != nums[i]:
                return i + 1
        return nums_len + 1

    def solve_2(self, nums: List[int]) -> int:
        """:returns

        """

        nums_len = len(nums)

        if 1 not in nums:
            # O(n)
            return 1

        if nums_len == 1:
            return 2

        for index in range(nums_len):
            # 用1 替换 小于等于0  和 大于数组长度的数
            if nums[index] <= 0 or nums[index] > nums_len:
                nums[index] = 1

        for index in range(nums_len):
            val = abs(nums[index])

            if val == nums_len:
                nums[0] = - abs(nums[0])
            else:
                nums[val] = - abs(nums[val])

        for i in range(1, nums_len):
            if nums[i] > 0:
                return i

        if nums[0]>0:
            return nums_len

        return nums_len + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
