"""
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
        输入: ["flower","flow","flight"]
        输出: "fl"

    示例 2:
        输入: ["dog","racecar","car"]
        输出: ""

    解释: 输入不存在公共前缀。
    说明: 所有输入只包含小写字母 a-z 。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        if strs:
            # 1.找出长度最小的字符串
            min_size_s = strs[0]
            for s in strs[1:]:
                if len(min_size_s) > len(s):
                    min_size_s = s

            min_size = len(min_size_s)
            # 2.遍历整个字符串数组
            for s in strs:
                index = 0
                # 2.1 判断是否有公共前缀
                while 0 <= index < min_size and min_size_s[index] == s[index]:
                    index += 1

                if index == 0:
                    res = ""
                    break
                else:
                    # 3 更新公共前缀 
                    res = min(res, min_size_s[:index]) if res != "" else min_size_s[:index]
        return res


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["aac", "ab"]))
