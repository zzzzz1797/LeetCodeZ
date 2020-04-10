"""
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    示例 1：
        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。

    示例 2：
        输入: "cbbd"
        输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

    @classmethod
    def dp(cls, s: str) -> str:
        """
            dp[i,j]  代表s[i,j]是否为回文串
            dp[i, j] = s[i]==s[j] and dp[i+1][j-1]
            当j-1 - (i+1) +1>2时 才会够成一个完整的区间
            当s[i, j]的长度等于2或者3时，只需要判断 s[i-1] s[j+1]

            时间复杂度：O(n^2)
            空间复杂度：O(n^2)
        """
        size = len(s)
        dp = [[False for i in range(size)] for j in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for i in range(1, size):
            for j in range(0, i):
                if s[i] == s[j]:
                    if i - j < 3:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j + 1][i - 1]
                else:
                    dp[j][i] = False

                if dp[j][i] is True:
                    cur_len = i - j + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = j
        return s[start: start + max_len]

    @classmethod
    def center_and_double_pointer(cls, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        res = s[0]

        def compute(x, y):
            while x >= 0 and y < size and s[x] == s[y]:
                x -= 1
                y += 1
            return s[x + 1:y]

        for i in range(size):
            odd_str = compute(i, i)
            even_str = compute(i, i + 1)

            res = max(odd_str, even_str, res, key=len)
        return res
