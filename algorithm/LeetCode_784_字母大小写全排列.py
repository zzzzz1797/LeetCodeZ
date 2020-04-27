"""
    给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

    示例:
        输入: S = "a1b2"
        输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

        输入: S = "3z4"
        输出: ["3z4", "3Z4"]

        输入: S = "12345"
        输出: ["12345"]
    注意：
        S 的长度不超过12。
        S 仅由数字和字母组成。
"""

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        pass

    @classmethod
    def solve_1(cls, S: str) -> List[str]:
        res = [[]]

        for char in S:
            n = len(res)
            if char.isalpha():
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(char.upper())
                    res[n + i].append(char.lower())
            else:
                for i in range(n):
                    res[i].append(char)
        return list(map("".join, res))

    @classmethod
    def solve_2(cls, S: str) -> List[str]:
        size = len(S)
        res = []

        def helper(info, index):
            if index > size:
                return
            if index == size:
                res.append(info)
                return

            # 未修改当前位置的元素
            helper(info, index + 1)

            # 修改了当前位置的元素
            if info[index].isalpha():
                if info[index].islower():
                    helper(info[:index] + info[index].upper() + info[index + 1:], index + 1)
                else:
                    helper(info[:index] + info[index].lower() + info[index + 1:], index + 1)

        helper(S, 0)
        return res


if __name__ == '__main__':
    print(Solution.solve_2("a1b2"))
