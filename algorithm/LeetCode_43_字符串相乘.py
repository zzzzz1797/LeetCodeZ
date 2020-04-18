"""
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

    示例 1:
        输入: num1 = "2", num2 = "3"
        输出: "6"

    示例 2:
        输入: num1 = "123", num2 = "456"
        输出: "56088"
    说明：

        num1 和 num2 的长度小于110。
        num1 和 num2 只包含数字 0-9。
        num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + carry
                carry = (res[i + j + 1] + tmp) // 10
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10
            res[i] += carry

        res = "".join(map(str, res))
        return "0" if not (ret := res.lstrip("0")) else ret


if __name__ == '__main__':
    print(Solution().multiply("1234", "45"))
