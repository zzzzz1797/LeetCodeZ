"""
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
    说明：
        拆分时可以重复使用字典中的单词。
        你可以假设字典中没有重复的单词。

    示例 1：
        输入: s = "leetcode", wordDict = ["leet", "code"]
        输出: true
        解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

    示例 2：
        输入: s = "applepenapple", wordDict = ["apple", "pen"]
        输出: true
        解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
            注意你可以重复使用字典中的单词。
    示例 3：
        输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
        输出: false
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass

    @classmethod
    def recursive(cls, s: str, wordDict: List[str]) -> bool:
        size = len(s)

        @lru_cache(None)
        def helper(index):
            # 递归的终止条件
            if index == size:
                return True

            # 业务逻辑
            for i in range(index + 1, size + 1):
                if s[index:i] in wordDict and helper(i):
                    return True
            return False

        return helper(0)

    @classmethod
    def dp_1(cls, s: str, wordDict: List[str]) -> bool:
        """
            dp 长度为s的size+1
            dp[i] 表示 s的前i位是否可以用wordDict中的单词表示
            dp[0] = True


        """
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True

        for i in range(size):
            for j in range(i + 1, size + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

        if __name__ == '__main__':
            print(Solution().recursive("leetcode", ["leet", "code"]))
