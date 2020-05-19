"""
    给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
    注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

    示例 1：
        输入：
          s = "barfoothefoobarman",
          words = ["foo","bar"]
        输出：[0,9]
        解释：
            从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
            输出的顺序不重要, [9,0] 也是有效答案。

    示例 2：
        输入：
          s = "wordgoodgoodgoodbestword",
          words = ["word","good","best","word"]
        输出：[]
"""
from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass

    @classmethod
    def solve_1(cls, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_size = len(words[0])
        total_size = len(words) * word_size
        s_size = len(s)
        words = Counter(words)
        res = []
        for i in range(0, s_size - total_size + 1):
            tmp = s[i:i + total_size]
            c_tmp = []
            for j in range(0, total_size, word_size):
                c_tmp.append(tmp[j:j + word_size])
            if Counter(c_tmp) == words:
                res.append(i)
        return res


if __name__ == '__main__':
    print(Solution.solve_1("barfoothefoobarman", ["foo", "bar"]))
