"""
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
    整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""

MAX_VAL = 2 ** 31 - 1
MIN_VAL = -2 ** 31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        if divisor == 1:
            if sign == 1:
                return min(MAX_VAL, dividend)
            else:
                return max(MIN_VAL, dividend)

        if divisor == -1:
            if sign == 1:
                print('ssss', MIN_VAL, )
                return min(MAX_VAL, -dividend)
            else:
                return max(MIN_VAL, -dividend)

        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            temp = b
            count = 1

            while (temp << 1) <= a:
                temp <<= 1
                count <<= 1
            a -= temp
            res += count
        if sign == 1:
            return min(res, MAX_VAL)
        else:
            return max(-res, MIN_VAL)


if __name__ == '__main__':
    print(Solution().divide(-2147483648, -1))
