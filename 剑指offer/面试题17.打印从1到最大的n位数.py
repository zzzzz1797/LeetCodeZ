"""
    输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
    示例 1:
        输入: n = 1
        输出: [1,2,3,4,5,6,7,8,9]
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_info = 0

        i = 0
        while n:
            max_info = max_info + 9 * (10 ** i)
            i += 1
            n = n - 1
        print(max_info)


if __name__ == '__main__':
    Solution().printNumbers(8)
