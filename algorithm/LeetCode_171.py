"""
    给定一个Excel表格中的列名称，返回其相应的列序号。
    例如，

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...

    示例 1:
        输入: "A"
        输出: 1

    示例 2:
        输入: "AB"
        输出: 28

    示例 3:
        输入: "ZY"
        输出: 701
"""

from string import ascii_uppercase


class Solution:
    base_val_dict = {ascii_uppercase[i - 1]: i for i in range(1, 27)}

    def titleToNumber(self, s: str) -> int:
        res = 0
        for s_one in s:
            res = res * 26 + self.base_val_dict[s_one]
        return res


if __name__ == '__main__':
    print(Solution().titleToNumber("AAA"))
