"""
    两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
    给出两个整数 x 和 y，计算它们之间的汉明距离。

    注意：
        0 ≤ x, y < 231.

    示例:
        输入: x = 1, y = 4

        输出: 2

        解释:
        1   (0 0 0 1)
        4   (0 1 0 0)
               ↑   ↑
    上面的箭头指出了对应二进制位不同的位置。
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
            汉明距离：两个字符串对应位置的不同字符的个数，也就是说将一个字符串变换称另一个字符串所需要的个数。
        """
        target = x ^ y

        res = 0
        while target:
            if target & 1 == 1:
                res += 1
            target = target >> 1
        return res


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))
