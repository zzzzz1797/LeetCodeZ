"""
    给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
    你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
    此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

    示例:
        s = "3[a]2[bc]", 返回 "aaabcbc".
        s = "3[a2[c]]", 返回 "accaccacc".
        s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    NUMS = tuple(map(str, range(9)))

    def decodeString(self, s: str) -> str:
        pass

    @classmethod
    def solve_1(cls, s: str) -> str:
        stack = []

        for index, row in enumerate(s):
            if row == "]":
                # 出栈做处理
                tmp_inf = ""
                tmp_num = ""

                # 处理字母
                while stack[-1] != "[":
                    tmp_inf = stack.pop() + tmp_inf

                # 走到这里应该弹出"["
                stack.pop()

                # 处理数字,只有不是数字时跳出循环。
                while stack and stack[-1] in cls.NUMS:
                    tmp_num = stack.pop() + tmp_num
                tmp_inf = tmp_inf * int(tmp_num)
                stack.append(tmp_inf)
            else:
                # 入栈处理
                stack.append(row)

        return "".join(stack)


if __name__ == '__main__':
    print(Solution.solve_1("3[a]2[bc]"))
