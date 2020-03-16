"""
    给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
    假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
    注意：每次拼写时，chars 中的每个字母都只能用一次。
    返回词汇表 words 中你掌握的所有单词的 长度之和。

    示例 1：
        输入：words = ["cat","bt","hat","tree"], chars = "atach"
        输出：6
        解释：可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

    示例 2：
        输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
        输出：10
        解释：
        可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
 
    提示：
        1 <= words.length <= 1000
        1 <= words[i].length, chars.
"""
from typing import List, Dict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 1. 转换chars为一个哈希表 key 为char value为cnt
        chars_cnt_dict = self.word_cnt_statistics(chars)

        # 2. 遍历words 判断word 是否可以由chars_cnt_dict 组成
        res = 0
        for word in words:
            word_cnt_dict = self.word_cnt_statistics(word)
            flag = True
            for char in word:
                if word_cnt_dict[char] > chars_cnt_dict.get(char, 0):
                    flag = False
                    break
            if flag:
                res += len(word)
        return res

    @classmethod
    def word_cnt_statistics(cls, word: str) -> Dict[str, int]:
        chars_cnt_dict = {}
        for char in word:
            chars_cnt_dict[char] = chars_cnt_dict.get(char, 0) + 1
        return chars_cnt_dict
