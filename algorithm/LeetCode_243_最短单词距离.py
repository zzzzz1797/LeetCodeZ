"""
    给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。
    示例:
        假设 words = ["practice", "makes", "perfect", "coding", "makes"]
        输入: word1 = “coding”, word2 = “practice”
        输出: 3
        输入: word1 = "makes", word2 = "coding"
        输出: 1
    注意:
        你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
"""
from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        res = second_index = first_index = float("inf")

        for index, word in enumerate(words):
            if word == word1:
                first_index = index
                res = min(res, abs(first_index - second_index))
            if word == word2:
                second_index = index
                res = min(res, abs(first_index - second_index))
        return res


if __name__ == '__main__':
    print(Solution().shortestDistance(["a", "a", "b", "b"], "a", "b"))
