"""
    给定一个字符串s，找出至多包含k 个不同字符的最长子串 T。
    示例 1:
        输入: s = "eceba", k = 2
        输出: 3
        解释: 则 T 为 "ece"，所以长度为 3。

    示例 2:
        输入: s = "aa", k = 1
        输出: 2
        解释: 则 T 为 "aa"，所以长度为 2。
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        pass

    @classmethod
    def solve_1(cls, s: str, k: int) -> int:
        size = len(s)
        if size < 3:
            # 特判
            return size

        # 定义窗口的左右边界
        left = right = 0

        # 定义窗口的内容
        windows = {}
        res = 2

        while right < size:

            windows[s[right]] = right

            # 窗口满足了，判断窗口里面的内容
            if len(windows) > k:
                # 删除窗口中最小的那个值
                min_index = min(windows.values())
                del windows[s[min_index]]
                left = min_index + 1
            res = max(res, right - left + 1)
            right += 1
        return res
