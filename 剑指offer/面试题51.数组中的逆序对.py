"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
    输入: [7,5,6,4]
    输出: 5
"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pass

    @classmethod
    def solve_1(cls, nums: List[int]) -> int:
        """
            暴力破解
            时间复杂度：O(n^2)
            空间复杂度：O(1)
        """

        size = len(nums)
        res = 0

        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] > nums[j]:
                    res += 1
        return res

    @classmethod
    def solve_2(cls, nums: List[int]) -> int:
        res = cls.merge_sort(nums, [0] * len(nums), 0, len(nums) - 1)
        print(nums)
        return res

    @classmethod
    def merge_sort(cls, nums: List[int], tmp_nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        cnt = cls.merge_sort(nums, tmp_nums, left, mid) + cls.merge_sort(nums, tmp_nums, mid + 1, right)

        i = left
        j = mid + 1
        pos = left

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                print(nums[i], nums[j], mid)
                tmp_nums[pos] = nums[i]
                i += 1
                cnt += (j - mid - 1)
            else:
                tmp_nums[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            tmp_nums[pos] = nums[k]
            cnt += (j - mid - 1)
            pos += 1

        for k in range(j, right + 1):
            tmp_nums[pos] = nums[k]
            pos += 1

        nums[left:right + 1] = tmp_nums[left:right + 1]
        return cnt


if __name__ == '__main__':
    print(Solution().solve_1([7, 5, 1, 6, 3, 4]))
    print(Solution().solve_2([7, 5, 1, 6, 3, 4]))
