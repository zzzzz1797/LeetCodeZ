"""
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
    序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
    示例 1：
        输入：target = 9
        输出：[[2,3,4],[4,5]]

    示例 2：
        输入：target = 15
        输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 
    限制：
        1 <= target <= 10^5
"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = j = 1
        tmp_target = 0
        res = []

        while i <= target // 2:
            if tmp_target < target:
                tmp_target += j
                j += 1
            elif tmp_target > target:
                tmp_target -= i
                i += 1
            else:
                res.append(list(range(i, j)))
                tmp_target -= i
                i += 1
        return res
