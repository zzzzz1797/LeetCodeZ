"""
    给一非空的单词列表，返回前 k 个出现次数最多的单词。
    返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

    示例 1：
        输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
        输出: ["i", "love"]
        解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
        注意，按字母顺序 "i" 在 "love" 之前。
 
    示例 2：
        输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
        输出: ["the", "is", "sunny", "day"]
        解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
        出现次数依次为 4, 3, 2 和 1 次。

"""

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass

    @classmethod
    def solve_1(cls, words: List[str], k: int) -> List[str]:
        # key为单词 value为出现的频次
        freq_dict = {}
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1
        # 以出现的频次为序
        bucket_dict = {}

        max_cnt = float("-inf")
        for word, cnt in freq_dict.items():
            bucket_dict[cnt] = bucket_dict.get(cnt, []) + [word]
            max_cnt = max(max_cnt, cnt)

        print(bucket_dict, "ff", max_cnt)

        res = []
        for i in range(max_cnt, 0, -1):
            if i in bucket_dict:
                res += sorted(bucket_dict[i])

            if len(res) > k:
                break
        return res[:k]


if __name__ == '__main__':
    print(Solution().solve_1(["i", "love", "leetcode", "i", "love", "coding"], 1))
