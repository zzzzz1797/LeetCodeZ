"""
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
    示例 1:
        输入: 123
        输出: 321

    示例 2:
        输入: -123
        输出: -321

    示例 3:
        输入: 120
        输出: 21

    注意:
        假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            return -self.reverse(-x)

        while x:
            # 求出最后一位
            tmp_res = x % 10
            # 抛弃最后一位
            x = x // 10
            # 从最后一位开始向前叠加
            res = res * 10 + tmp_res

            if not self.is_safe(res):
                return 0
        return res

    @classmethod
    def is_safe(cls, data: int) -> bool:
        return -2 ** 31 <= data <= 2 ** 31 - 1


if __name__ == '__main__':
    print(Solution().reverse(123))
