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
            print(i, usedChar, start)
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
                print(usedChar[s[i]], start , "ss")
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcdafg"))
