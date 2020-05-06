"""
    在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
    给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）

    例子:
        输入: N = 1, K = 1
        输出: 0

        输入: N = 2, K = 1
        输出: 0

        输入: N = 2, K = 2
        输出: 1

        输入: N = 4, K = 5
        输出: 1

    解释:
    第一行: 0
    第二行: 0 1
    第三行: 0 1 1 0
    第四行: 0 1 1 0 1 0 0 1
"""


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return self.recursive(N, K)

    @classmethod
    def recursive(cls, N: int, K: int) -> int:
        """
            第K个数是上一行第 (K+1) //2
            如果K是偶数
        """
        if K == 1:
            return 0

        G = cls.recursive(N - 1, (K + 1) // 2)
        if K % 2 == 1:
            return G
        else:
            return 1 - G
