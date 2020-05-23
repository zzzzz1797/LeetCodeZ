"""
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
from typing import List


class Solution:
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        size = len(digits)

        def helper(index: int, tmp_res: str = "") -> None:
            if index == size:
                if tmp_res:
                    res.append(tmp_res)
                return

            for ch in self.mapping.get(digits[index], []):
                helper(index + 1, tmp_res + ch)

        helper(0)
        return res
