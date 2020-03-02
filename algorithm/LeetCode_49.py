"""
    给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

    示例:
        输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
        输出:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]

    说明：
        所有输入均为小写字母。
        不考虑答案输出的顺序。
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for s_one in s:
                count[ord(s_one) - ord('a')] += 1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())
