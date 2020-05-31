"""
        两个玩家分别扮演猫（Cat）和老鼠（Mouse）在无向图上进行游戏，他们轮流行动。
    该图按下述规则给出：graph[a] 是所有结点 b 的列表，使得 ab 是图的一条边。老鼠从结点 1 开始并率先出发，猫从结点 2 开始且随后出发，在结点0处
    有一个洞。在每个玩家的回合中，他们必须沿着与他们所在位置相吻合的图的一条边移动。 例如，如果老鼠位于结点 1，那么它只能移动到 graph[1] 中
    的（任何）结点去。此外，猫无法移动到洞（结点 0）里。

        然后，游戏在出现以下三种情形之一时结束：
            如果猫和老鼠占据相同的结点，猫获胜。
            如果老鼠躲入洞里，老鼠获胜。
            如果某一位置重复出现（即，玩家们的位置和移动顺序都与上一个回合相同），游戏平局。
        给定 graph，并假设两个玩家都以最佳状态参与游戏，如果老鼠获胜，则返回 1；如果猫获胜，则返回 2；如果平局，则返回 0。
"""
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        pass

    @classmethod
    def solve_1(cls, graph: List[List[int]]) -> int:
        """
            假设status是一个三位矩阵，表示状态转移。
                1、status[i][j][0] 表示老鼠在i位置，猫在j位置，并且此时轮到老鼠行动
                2、status[i][j][1] 表示老鼠在i位置，猫在j位置，并且次数轮到猫行动
                3、status[i][j][k] 的值，如果是0，则本剧游戏是平局。如果是1则代表老鼠胜。如果是2则代表猫胜利。
            默认情况下
                status[0][j][k] = 1，此时老鼠在洞里，老鼠肯定赢。
                status[i][i][k] = 2，当i不等于0的时候，老鼠和猫是同一位置，则猫肯定能赢。
        """
        length = len(graph)
        color = [[[0] * 3 for _ in range(length)] for _ in range(length)]
        q = []
        for i in range(1, length):
            for t in range(1, 3):
                color[0][i][t] = 1  # 老鼠胜利
                q.append((0, i, t))
                color[i][i][t] = 2  # 猫胜利
                q.append((i, i, t))
        while q:
            cur_status = q.pop(0)
            mouse, cat, turn = cur_status
            for pre_status in cls.find_prev_status(graph, cur_status):
                pre_mouse, pre_cat, pre_turn = pre_status
                if color[pre_mouse][pre_cat][pre_turn] != 0:
                    continue
                if color[mouse][cat][turn] == pre_turn:
                    color[pre_mouse][pre_cat][pre_turn] = pre_turn
                    q.append(pre_status)
                else:
                    # 默认color[cat][mouse][turn]==turn
                    if turn == 2:
                        # color[cat][mouse][2]=2如果color[cat][pre_mouse][1]=1 全部color[cat][next_pre_mouse][2]=2
                        flag = True
                        for next_pre_mouse in graph[pre_mouse]:
                            if color[next_pre_mouse][pre_cat][turn] != turn:
                                flag = False
                                break
                        if flag:
                            color[pre_mouse][pre_cat][pre_turn] = turn
                            q.append(pre_status)
                    else:
                        flag = True
                        for next_pre_cat in graph[pre_cat]:
                            if next_pre_cat == 0:
                                continue
                            if color[pre_mouse][next_pre_cat][turn] != turn:
                                flag = False
                                break
                        if flag:
                            color[pre_mouse][pre_cat][pre_turn] = turn
                            q.append(pre_status)
        return color[1][2][1]

    @classmethod
    def find_prev_status(cls, graph, cur_status):
        ret = []
        mouse, cat, turn = cur_status
        if turn == 1:
            for pre_cat in graph[cat]:
                if pre_cat == 0:
                    continue
                ret.append((mouse, pre_cat, 2))
        else:
            for pre_mouse in graph[mouse]:
                # 则上一轮pre_mouse,pre_cat=cat,pre_turn=1,找出能到mouse的点，就是graph[mouse]中的点。
                ret.append((pre_mouse, cat, 1))
        return ret
