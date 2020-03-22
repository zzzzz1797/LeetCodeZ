"""
    有两个容量分别为 x升 和 y升 的水壶以及无限多的水。
    请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

    如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

    你允许：
        装满任意一个水壶
        清空任意一个水壶
        从一个水壶向另外一个水壶倒水，直到装满或者倒空

    示例 1: (From the famous "Die Hard" example)

        输入: x = 3, y = 5, z = 4
        输出: True

    示例 2:
        输入: x = 2, y = 6, z = 5
        输出: False
"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return self.use_math(x, y, z)

    @classmethod
    def use_math(cls, x: int, y: int, z: int) -> bool:
        """
            ax + by = z
            根据祖定理原理 只要 z 是 x和y 最大公约数的倍数 就能灌满
        """

        def god(tmp_x, tmp_y):
            return tmp_x if tmp_y == 0 else god(tmp_y, tmp_x % tmp_y)

        if x + y < z:
            return False

        if x == 0 or y == 0 or z == 0:
            return x + y == z or z == 0

        return z % god(x, y) == 0

    @classmethod
    def use_dfs_by_stack(cls, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        visited = set()

        while stack:
            cur_x, cur_y = stack.pop()

            if cur_x == z or cur_y == z or cur_x + cur_y == z:
                return True

            if (cur_x, cur_y) in visited:
                continue
            visited.add((cur_x, cur_y))
            # 1、把x灌满
            stack.append((x, cur_y))

            # 2、把y管满
            stack.append((cur_x, y))

            # 3.把x倒空
            stack.append((0, cur_y))

            # 4.把y倒空
            stack.append((cur_x, 0))

            # 5. 把x的倒入y中，只倒y满了或者x空了
            tmp_x = cur_x - min(cur_x, y - cur_y)
            tmp_y = cur_y + min(cur_x, y - cur_y)
            stack.append((tmp_x, tmp_y))

            # 6. 把y的水倒入x中，只到x倒满或者x空了
            tmp_x = cur_x + min(cur_y, x - cur_x)
            tmp_y = cur_y - min(cur_y, x - cur_x)
            stack.append((tmp_x, tmp_y))
        return False


if __name__ == '__main__':
    print(Solution.use_math(3, 5, 4), "fff")
