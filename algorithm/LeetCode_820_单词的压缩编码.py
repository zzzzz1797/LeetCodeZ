"""
    给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
    例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
    对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
    那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

    示例：
        输入: words = ["time", "me", "bell"]
        输出: 10
        说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
    提示：
        1 <= words.length <= 2000
        1 <= words[i].length <= 7
        每个单词都是小写字母 。
"""
from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.end_flag = "#"

    def insert(self, word: str) -> bool:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        new_word_flag = True if not node else False
        node[self.end_flag] = self.end_flag
        return new_word_flag

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_flag in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
            1、构建一个trie树，修改一下trie树的插入方法，当是一个新词（不能被之前覆盖）插入时返回True，否则返回 False。
            2、给定的单词列表按照长度的大小，从大到小开始排列。
            3、遍历排好序的单词列表，依次插入到trie树中，插入之前反转单词。
            4、判断插入的返回结果，如果是新的则结果增加 单词长度+1

            时间复杂度：O(∑w i) 其中 wi是 words[i] 的长度。对于每个单词中的每个字母，只需要进行常数次操作。
            空间复杂度：O(S∗∑wi)，字典树的空间开销，其中 S 为字符集大小。
        """

        trie = Trie()
        words.sort(key=lambda key: len(key), reverse=True)

        res = 0
        for word in words:
            new_word_flag = trie.insert(word[::-1])
            res += len(word) + 1 if new_word_flag else 0

        return res


if __name__ == '__main__':
    print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
