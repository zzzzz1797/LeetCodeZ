"""
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。

    说明：
        所有数字（包括 target）都是正整数。
        解集不能包含重复的组合。 

    示例 1:
        输入: candidates = [2,3,6,7], target = 7,
        所求解集为:
            [
              [7],
              [2,2,3]
            ]

    示例 2:
        输入: candidates = [2,3,5], target = 8,
        所求解集为:
            [
              [2,2,2,2],
              [2,3,3],
              [3,5]
            ]
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solve_1(candidates, target)

    @classmethod
    def solve_1(cls, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 先排下序  为了提高匹配效率
        res = []
        size = len(candidates)

        def helper(index, tmp_sum, tmp_res):
            if tmp_sum == target:
                # 这里需要返回 否则会出现重复结果集
                res.append(tmp_res)
                return res
            if tmp_sum > target and index == size:
                return

            # 继续使用当前元素
            helper(index, tmp_sum + candidates[index], tmp_res + [candidates[index]])
            # 跳到下一个元素
            helper(index + 1, tmp_sum, tmp_res)

        helper(0, 0, [])
        return res

    @classmethod
    def solve_2(cls, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        size = len(candidates)
        candidates.sort()

        def helper(index, tmp_res, tmp_target):
            if tmp_target == 0:
                res.append(tmp_res)
                return

            for i in range(index, size):
                if candidates[i] > tmp_target:
                    break
                helper(i, tmp_res + [candidates[i]], tmp_target - candidates[i])

        helper(0, [], target)
        return res
