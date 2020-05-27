"""
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

    请找出其中最小的元素。
        你可以假设数组中不存在重复元素。

        示例 1:
            输入: [3,4,5,1,2]
            输出: 1

        示例 2:
            输入: [4,5,6,7,0,1,2]
            输出: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

    @classmethod
    def solve_1(cls, nums: List[int]) -> int:
        """
            为什么左右不对称？只比较mid与right?
            https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))
