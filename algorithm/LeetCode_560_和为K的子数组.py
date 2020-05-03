"""
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

    示例 1 :
        输入:nums = [1,1,1], k = 2
        输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

    说明 :
        数组的长度为 [1, 20,000]。
        数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {0: 1}

        res = total = 0
        for num in nums:
            total += num

            other_num = total - k
            print(total, other_num)
            if other_num in mapping:
                res += mapping[other_num]
            mapping[total] = mapping.get(total, 0) + 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))
