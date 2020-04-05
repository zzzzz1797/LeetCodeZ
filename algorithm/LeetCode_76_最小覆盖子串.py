"""
    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

    示例：
        输入: S = "ADOBECODEBANC", T = "ABC"
        输出: "BANC"
    说明：
        如果 S 中不存这样的子串，则返回空字符串 ""。
        如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            滑动窗口解法
                时间复杂度：O(m+n)
                空间复杂度：O(m+n)
        """

        lookup = collections.defaultdict(int)

        for char in t:
            lookup[char] += 1

        left = right = 0
        max_len = float("inf")
        res = ""
        cnt = len(t)

        while right <= len(s) - 1:
            char = s[right]
            if lookup[char] > 0:
                cnt -= 1
            lookup[char] -= 1
            right += 1

            while cnt == 0:
                if right - left < max_len:
                    max_len = right - left
                    res = s[left:right]
                if lookup[s[left]] == 0:
                    cnt += 1
                lookup[s[left]] += 1
                left += 1

        return res


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
