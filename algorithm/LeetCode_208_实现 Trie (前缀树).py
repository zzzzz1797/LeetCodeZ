"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
"""
from typing import Dict, Optional


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self._end_flag = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for ch in word:
            root = root.setdefault(ch, {})
        root[self._end_flag] = self._end_flag

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        return True if (root := self._common_search(word)) and self._end_flag in root else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        return True if self._common_search(prefix) else False

    def _common_search(self, word: str) -> Optional[Dict]:
        root = self.root
        for ch in word:
            root = root.get(ch)
            if not root:
                break
        else:
            return root
