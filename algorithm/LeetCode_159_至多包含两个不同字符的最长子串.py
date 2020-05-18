"""
    给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

    示例 1:
        输入: "eceba"
        输出: 3
        解释: t 是 "ece"，长度为3。
    
    示例 2:
        输入: "ccaabbb"
        输出: 5
        解释: t 是 "aabbb"，长度为5。
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        pass

    @classmethod
    def solve_1(cls, s: str) -> int:
        """
            滑动窗口
        """
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
            if len(windows) > 2:

                # 删除窗口中最小的那个值
                min_index = min(windows.values())
                del windows[s[min_index]]
                left = min_index + 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    print(Solution().solve_1("ccaabbb"))
