"""
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

    说明:
        s 可能为空，且只包含从 a-z 的小写字母。
        p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

    示例 1:
        输入:
            s = "aa"
            p = "a"
        输出: false
        解释: "a" 无法匹配 "aa" 整个字符串。

    示例 2:
        输入:
            s = "aa"
            p = "a*"
        输出: true
        解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
    示例 3:
        输入:
            s = "ab"
            p = ".*"
        输出: true
        解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass

    @classmethod
    def dp(cls, s: str, p: str) -> bool:
        """
            dp[i][j] ：s前i个字符[0,i)是否能匹配p的前j个字符[0,j)

            s[i-1]==p[j-1]:  dp[i][j] = dp[i-1][j-1]

            s[i-1]!=p[j-1]
                p[j-1]=='.'    dp[i][j] = dp[i-1][j-1]

                p[j-1]=='*'   取决于前面
        """
        s_size = len(s)
        p_size = len(p)

        dp = [[False for i in range(p_size + 1)] for j in range(s_size + 1)]
        dp[0][0] = True

        for j in range(2, p_size + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, s_size + 1):
            for j in range(1, p_size + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == ".":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == "*":
                        if j >= 2:
                            if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                                dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                            else:
                                dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]

    @classmethod
    def recursive(cls, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = s and p[0] in (s[0], ".")

        if len(p) >= 2 and p[1] == "*":
            return cls.recursive(s, p[2:]) or (first_match and cls.recursive(s[1:], p))
        else:
            return first_match and cls.recursive(s[1:], p[1:])


if __name__ == '__main__':
    print(Solution.dp("aa", "a"))
    print(Solution.recursive("aa", "a"))
