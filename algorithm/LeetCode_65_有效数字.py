"""
    验证给定的字符串是否可以解释为十进制数字。

    例如:
        "0" => true
        " 0.1 " => true
        "abc" => false
        "1 a" => false
        "2e10" => true
        " -90e3   " => true
        " 1e" => false
        "e3" => false
        " 6e-1" => true
        " 99e2.5 " => false
        "53.5e93" => true
        " --6 " => false
        "-+3" => false
        "95a54e53" => false
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        pass

    @classmethod
    def solve_1(cls, s: str) -> bool:
        s = s.strip()  # 去除首位空格

        # 定义 字母e是否查看过了，数字是否查看过了，小数点是否查看过了
        e_seen = num_seen = dot_seen = False

        for index, s_one in enumerate(s):
            if s_one.isdigit():
                num_seen = True
            elif s_one == ".":
                # 有点的话，前面不能出现.或者e
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            elif s_one == "e":
                # 有字母e的话，前面不能再出现e，而且前面必须出现数字
                if e_seen or not num_seen:
                    return False

                # 并且出现e后，则后面必须再出现数字 像0e这种其实是非法
                num_seen = False
                e_seen = True
            elif s_one in "+-":
                # 如果出现符合，并且没有在首位出现，则符号后面前面必须跟一个e
                if index > 0 and s[index - 1] != "e":
                    return False
            else:
                return False
        return num_seen


if __name__ == '__main__':
    print(Solution.solve_1("-1."))
