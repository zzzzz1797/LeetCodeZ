"""
    一条包含字母 A-Z 的消息通过以下方式进行了编码：

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。

    示例 1:
        输入: "12"
        输出: 2
        解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

    示例 2:
        输入: "226"
        输出: 3
        解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        if s:
            if s[0] == "0":
                return res
            pre = cur = 1

            for i in range(1, len(s)):
                tmp = cur

                if s[i] == '0':
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        cur = pre
                    else:
                        return res
                elif s[i - 1] == '1' or (s[i - 1] == '2' and '1' <= s[i] <= '6'):
                    cur += pre
                pre = tmp
            res = cur

        return res
