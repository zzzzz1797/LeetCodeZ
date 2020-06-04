"""
        给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。
    每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
    给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

    示例 1:
        输入: [1, 5, 2]
        输出: False
        解释: 一开始，玩家1可以从1和2中进行选择。
        如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
        所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
        因此，玩家1永远不会成为赢家，返回 False。

    示例 2:
        输入: [1, 5, 233, 7]
        输出: True
        解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
        最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。
"""

from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        pass

    @classmethod
    def solve_1(cls, nums: List[int]) -> bool:
        """递归"""

        def helper(left: int, right: int, score_a: int, score_b: int, turn: bool):
            """
                left:   左边可以取的位置
                right:  右边可以取的文职
                score_a:    a的得分
                score_b:    b的得分
                turn:   谁的回合  true 表示是a的回合， false表示是b的回合
            """
            if left > right:
                return score_a >= score_b

            if turn:
                left_res = helper(left + 1, right, score_a + nums[left], score_b, False)
                right_res = helper(left, right - 1, score_a + nums[right], score_b, False)
                return left_res or right_res
            else:
                left_res = helper(left + 1, right, score_a, score_b + nums[left], True)
                right_res = helper(left, right - 1, score_a, score_b + nums[right], True)
                return left_res and right_res

        return helper(0, len(nums) - 1, 0, 0, True)

    @classmethod
    def solve_2(cls, nums: List[int]) -> bool:
        """
            dp[i][j]表示先手玩家的在[i,j]范围内获取到的最大分数
        """


