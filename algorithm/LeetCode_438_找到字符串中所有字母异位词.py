"""
    给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
    字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
    说明：
        字母异位词指字母相同，但排列不同的字符串。
        不考虑答案输出的顺序。
    示例 1:
        输入:
            s: "cbaebabacd" p: "abc"
        输出:
            [0, 6]
        解释:
            起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
            起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
    示例 2:
        输入:
            s: "abab" p: "ab"
        输出:
            [0, 1, 2]
        解释:
            起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
            起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
            起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_list = [ord(i) - 97 for i in s]
        p_list = [ord(i) - 97 for i in p]
        hash_list = [0] * 26

        s_len = len(s)
        p_len = len(p)

        left = right = count = 0
        res = []

        for i in range(p_len):
            hash_list[p_list[i]] += 1

        while right < s_len:
            hash_list[s_list[right]] -= 1
            if hash_list[s_list[right]] >= 0:
                count += 1
            print(right, p_len - 1)
            if right > p_len - 1:
                hash_list[s_list[left]] += 1
                if hash_list[s_list[left]] > 0:
                    count -= 1
                left += 1

            if count == p_len:
                res.append(left)
            right += 1
        return res


if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
