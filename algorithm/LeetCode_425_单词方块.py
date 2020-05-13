"""
    给定一个单词集合 （没有重复），找出其中所有的 单词方块 。
    一个单词序列形成了一个有效的单词方块的意思是指从第 k 行和第 k 列 (0 ≤ k < max(行数, 列数)) 来看都是相同的字符串。
    例如，单词序列 ["ball","area","lead","lady"] 形成了一个单词方块，因为每个单词从水平方向看和从竖直方向看都是相同的。
        b a l l
        a r e a
        l e a d
        l a d y

    注意：
        单词个数大于等于 1 且不超过 500。
        所有的单词长度都相同。
        单词长度大于等于 1 且不超过 5。
        每个单词只包含小写英文字母 a-z。
 
    示例 1：
        输入：
            ["area","lead","wall","lady","ball"]
        输出：
            [
              [ "wall",
                "area",
                "lead",
                "lady"
              ],
              [ "ball",
                "area",
                "lead",
                "lady"
              ]
            ]
        解释：
            输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。

    示例 2：
        输入：
        ["abat","baba","atan","atal"]
        输出：
        [
          [ "baba",
            "abat",
            "baba",
            "atan"
          ],
          [ "baba",
            "abat",
            "baba",
            "atal"
          ]
        ]
    解释：
        输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。
"""
from typing import List, Dict


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        pass

    def solve_1(self, words: List[str]) -> List[List[str]]:
        """
            https://leetcode-cn.com/problems/word-squares/solution/dan-ci-fang-kuai-by-leetcode/
            思路：
                1、遍历给定列表
                2、以每一个元素作为第一行
                3、然后第二行应该是以第一行的第二列开头的的字母，所以找出这个以字母开头的所有字母，再去补全第二行
        """
        result = []
        self.word_len = len(words[0])
        self.words = words

        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, result)
        return result

    def backtracking(self, step, word_squares, result):
        if step == self.word_len:
            result.append(word_squares[:])
            return

        prefix = "".join([word[step] for word in word_squares])
        for candidate in self.get_word_with_prefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step + 1, word_squares, result)
            word_squares.pop()

    def get_word_with_prefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word


class SolutionV2:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = self.build_trie(words)
        res = []
        for word in words:
            self.backup(trie, words, 1, [word], res)
        return res

    @classmethod
    def backup(cls, trie, words, step, tmp_res, res):
        if step == len(words[0]):
            res.append(tmp_res[:])
            return

        prefix = "".join([word[step] for word in tmp_res])
        for tmp_word in cls.get_words_with_prefix_by_trie(words, trie, prefix):
            tmp_res.append(tmp_word)
            cls.backup(trie, words, step + 1, tmp_res, res)
            tmp_res.pop()

    @classmethod
    def get_words_with_prefix_by_trie(cls, words, trie, prefix):
        root = trie
        for ch in prefix:
            if ch not in root:
                return []
            else:
                root = root[ch]
        return [words[index] for index in root["#"]]

    @classmethod
    def build_trie(cls, words: List[str]) -> Dict:
        """
            构建一颗trie树
                trie树里面包含两个元素 一个是下个元素的引用， 一个是当前单词处在单词列表的哪个索引
        """
        trie = {}

        for index, word in enumerate(words):
            node = trie
            for ch in word:
                if ch in node:
                    node = node[ch]
                else:
                    new_node = {"#": []}
                    node[ch] = new_node
                    node = new_node
                node["#"].append(index)
        return trie


if __name__ == "__main__":
    # print(Solution().solve_1(["abat", "baba", "atan", "atal"]))
    # print(Solution().solve_2(["abat", "baba", "atan", "atal"]))
    print(Solution().build_trie(["abat", "bfbf", "bfbf"]))
