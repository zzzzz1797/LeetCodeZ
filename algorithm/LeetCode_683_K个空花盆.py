"""
    花园里有 N 个花盆，每个花盆里都有一朵花。这 N 朵花会在 N 天内依次开放，每天有且仅有一朵花会开放并且会一直盛开下去。
    给定一个数组 flowers 包含从 1 到 N 的数字，每个数字表示在那一天开放的花所在的花盆编号。

    例如， flowers[i] = x 表示在第 i 天盛开的花在第 x 个花盆中，i 和 x 都在 1 到 N 的范围内。
    给你一个整数 k，请你输出在哪一天恰好有两朵盛开的花，他们中间间隔了 k 朵花并且都没有开放。
    如果不存在，输出 -1。

    样例 1:
        输入:
            flowers: [1,3,2]
            k: 1
        输出: 2
        解释: 在第二天，第一朵和第三朵花都盛开了。
 
    样例 2:
        输入:
            flowers: [1,2,3]
            k: 1
        输出: -1
"""
from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        pass

    @classmethod
    def solve_1(cls, bulbs: List[int], K: int) -> int:
        # 第i盆开花的时间
        days = [0] * (len(bulbs) + 1)
        for index, row in enumerate(bulbs):
            days[row] = index + 1

        result = float("inf")
        left = 1
        right = left + K + 1

        while right < len(days):

            for i in range(left + 1, right):
                if days[i] <= days[left] or days[i] <= days[right]:
                    left = i
                    right = left + K + 1
                    break
            else:
                cur_result = max(days[left], days[right])
                result = min(result, cur_result)
                left = right
                right = left + K + 1
        return result if result != float("-inf") else 1
