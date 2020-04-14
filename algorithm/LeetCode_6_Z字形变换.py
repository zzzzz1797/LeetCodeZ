"""
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
        L   C   I   R
        E T O E S I I G
        E   D   H   N
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

    请你实现这个将字符串进行指定行数变换的函数：
        string convert(string s, int numRows);
    示例 1:

        输入: s = "LEETCODEISHIRING", numRows = 3
        输出: "LCIRETOESIIGEDHN"
    示例 2:

        输入: s = "LEETCODEISHIRING", numRows = 4
        输出: "LDREOEIIECIHNTSG"
        解释:
        L     D     R
        E   O E   I I
        E C   I H   N
        T     S     G
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass

    @classmethod
    def solve_1(cls, s: str, numRows: int) -> str:
        """
            其实就是上下来回走
            当开始从下走时，步长一直加一
            往上走时步长一直减一。
            怎么 判断是需要是需要加还是减，可以用一个临时变量保存步长的值，如果用负的步长来代表减法
        """
        if numRows == 1:
            return s
        res = ["" for i in range(numRows)]

        step_index = 0
        step_size = 0
        for row in s:
            if step_index == 0:
                step_size = 1
            elif step_index == numRows - 1:
                step_size = -1
            res[step_index] += row
            step_index += step_size
        return "".join(res)
