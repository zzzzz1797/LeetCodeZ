"""
    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

    示例：
        输入: S = "ADOBECODEBANC", T = "ABC"
        输出: "BANC"
    说明：
        如果 S 中不存这样的子串，则返回空字符串 ""。
        如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            滑动窗口解法
                时间复杂度：O(m+n)
                空间复杂度：O(m+n)
        """
        lookup = Counter(t)
        left = right = 0
        min_len = float("inf")
        res = ""
        s_size = len(s)
        t_size = len(t)

        while right < s_size:
            right_char = s[right]
            if lookup[right_char] > 0:
                t_size -= 1
            lookup[right_char] -= 1
            right += 1

            while t_size == 0:
                left_char = s[left]
                if right - left < min_len:
                    min_len = right - left
                    res = s[left:right]
                if lookup[left_char] == 0:
                    t_size += 1

                lookup[left_char] += 1
                left += 1
        return res

    @classmethod
    def solve(cls, s: str, t: str) -> str:
        if not t or not s:
            return ""
        t_counter = {}
        for t_one in t:
            t_counter[t_one] = t_counter.get(t_one, 0) + 1  # 统计t中元素出现的个数
        require_cnt = len(t_counter)
        left = right = 0  # 定义窗口的大小
        exist_cnt = 0  # 定义已经找到个数

        windows = {}

        res_cnt = float("inf")
        res = ""

        while right < len(s):
            ch = s[right]
            windows[ch] = windows.get(ch, 0) + 1

            if windows[ch] == t_counter.get(ch):
                exist_cnt += 1

            while left <= right and exist_cnt == require_cnt:
                ch = s[left]
                if right - left + 1 < res_cnt:
                    res_cnt = right - left + 1
                    res = s[left:right + 1]
                windows[ch] -= 1

                if windows[ch] < t_counter.get(ch, 0):
                    exist_cnt -= 1

                left += 1
            right += 1
        return res


if __name__ == '__main__':
    print(Solution().solve("aa", "aa"))
