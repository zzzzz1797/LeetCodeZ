"""
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:
        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    示例 2:
        输入: "bbbbb"
        输出: 1
        解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

    示例 3:

        输入: "pwwkew"
        输出: 3
        解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

    @classmethod
    def dp(cls, s):
        """
            动态规划
            dp[i] 表示是 以s[i]结尾的最长不重复子串
        """
        size = len(s)

        if size < 2:
            return size
        dp = [1 for i in range(size)]
        mapping = {s[0]: 0}

        for i in range(1, size):
            if s[i] in mapping:
                if dp[i - 1] >= i - mapping[s[i]]:
                    dp[i] = i - mapping[s[i]]
                else:
                    dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + 1
            mapping[s[i]] = i
        return max(dp)

    @classmethod
    def sliding_windows(cls, s):
        """
            滑动窗口
            思路：
                1、窗口的右边界先移动，直到窗口中出现重复的元素或者有边界已经超过了给定字符串的长度，在有有边界扩充的时候，记录最大值。
                2、当有边界停止时，移动左边界，直到窗口中没有重复的元素。跳转到第1步。
        """
        used = set()
        size = len(s)
        right = -1
        res = 0

        for i in range(size):
            if i != 0:
                used.remove(s[i - 1])
            while right + 1 < size and s[right + 1] not in used:
                right += 1
                used.add(s[right])
            res = max(res, right - i + 1)

        return res


if __name__ == '__main__':
    print(Solution().sliding_windows("abcdafg1"))
