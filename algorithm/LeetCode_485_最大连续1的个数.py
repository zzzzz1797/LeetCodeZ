"""
    给定一个二进制数组， 计算其中最大连续1的个数。
    示例 1:
        输入: [1,1,0,1,1,1]
        输出: 3
        解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
    注意：
        输入的数组只包含 0 和1。
        输入数组的长度是正整数，且不超过 10,000。
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = tmp_res = 0

        for num in nums:
            if num == 1:
                tmp_res += 1
            else:
                res = max(res, tmp_res)
                tmp_res = 0
        return max(res, tmp_res)
