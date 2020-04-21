"""
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
    示例: 
        输入: s = 7, nums = [2,3,1,2,4,3]
        输出: 2
        解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
    进阶:
        如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        pass

    @classmethod
    def solve_1(cls, s: int, nums: List[int]) -> int:
        """
            滑动窗口解法
            思路：
                1、定义一个滑动窗口 窗口左右边界初始化都是0
                2、移动窗口的右边界，每次移动都增加当前窗口内的数字和
                3、当数字和大于等于给定的s时，停止移动右边界。
                4、开始移动左边界，每次移动左边界的时候，更新结果集
                5、 循环 2 3 4 直到窗口的右边界到达数组的最后一位
            时间复杂度：O(n)
            空间复杂度：O(1)
        """
        res = float("inf")
        total = left = right = 0
        size = len(nums)

        while right < size:
            total += nums[right]

            while total >= s:
                res = min(right - left + 1, res)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if res == float('inf') else res

    @classmethod
    def solve_2(cls, s: int, nums: List[int]):
        """
            二分搜索
        """

        def mid_query(params, target):
            start = 0
            end = len(params) - 1
            while start <= end:
                mid = (start + end) >> 1
                mid_val = params[mid]
                if mid_val >= target:
                    if mid == 0 or params[mid - 1] < target:
                        return mid
                    else:
                        end = mid - 1
                else:
                    start = mid + 1
            return -1

        if not (size := len(nums)):
            return 0

        # 前缀和
        for i in range(1, size):
            nums[i] += nums[i - 1]

        # 判断是否有最后一位是否比目标小，如果最后一位都被目标小，则肯定没有能满足的元素
        if nums[-1] < s:
            return 0

        # 初始化 数据
        res = float("inf")
        nums = [0] + nums

        for i in range(len(nums)):
            index = mid_query(nums, nums[i] + s)
            if index >= 0 and index - i < res:
                res = index - i
        return 0 if res == float("inf") else res


if __name__ == '__main__':
    print(Solution().solve_2(7, [2, 3, 1, 2, 4, 3]))
