"""
    地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
    也不能进入行坐标和列坐标的数位之和大于k的格子。
    例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
    示例 1：
        输入：m = 2, n = 3, k = 1
        输出：3
        示例 1：

        输入：m = 3, n = 1, k = 0
        输出：1
        提示：

    1 <= n,m <= 100
    0 <= k <= 20
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        return self.bfs(m, n, k)

    @classmethod
    def bfs(cls, m: int, n: int, k: int) -> int:
        visited = set()

        res = 0
        queue = [(0, 0)]

        while queue:
            tmp_queue = []

            for i, j in queue:
                key = (i, j)
                if not (key not in visited and 0 <= i < m and 0 <= j < n and cls.get_sum(i) + cls.get_sum(j) <= k):
                    continue
                res += 1
                visited.add(key)

                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    tmp_queue.append((x + i, y + j))
            queue = tmp_queue
        return res

    @classmethod
    def dfs(cls, m: int, n: int, k: int) -> int:
        visited = set()
        res = 0

        def helper(row, col, ):
            nonlocal res
            key = (row, col)
            if not (0 <= row < m and 0 <= col < n and key not in visited and cls.get_sum(row) + cls.get_sum(col) <= k):
                return res
            visited.add(key)
            res += 1

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                helper(row + x, col + y)

        helper(0, 0)
        return res

    @classmethod
    def get_sum(cls, num: int) -> int:
        res = 0

        while num:
            res += num % 10
            num = num // 10
        return res


if __name__ == '__main__':
    print(Solution().dfs(2, 3, 1))
    print(Solution().bfs(2, 3, 1))
