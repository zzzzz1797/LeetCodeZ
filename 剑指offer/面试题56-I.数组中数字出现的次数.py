"""
    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
    示例 1：
        输入：nums = [4,1,4,6]
        输出：[1,6] 或 [6,1]

    示例 2：
        输入：nums = [1,2,10,4,1,4,3,3]
        输出：[2,10] 或 [10,2]
 
    限制：
        2 <= nums <= 10000
"""
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        pass

    @classmethod
    def solve_1(cls, nums: List[int]) -> List[int]:
        """
            & 按位与
            ^ 按位异或
            | 按位或
        """
        res = a = b = 0

        # 找出这只出现一次的两个数字的异或结果
        for num in nums:
            res ^= num

        # 找到第一位不是0的数
        h = 1
        while res & h == 0:
            h <<= 1

        # 分组
        for n in nums:
            if h & n == 0:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == '__main__':
    print(Solution().solve_1([4, 4, 4, 2, 1, 1, 4, 6]))
