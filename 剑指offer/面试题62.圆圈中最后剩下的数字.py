"""
    0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
    例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

    示例 1：
        输入: n = 5, m = 3
        输出: 3
    示例 2：
        输入: n = 10, m = 17
        输出: 2
    限制：

    1 <= n <= 10^5
    1 <= m <= 10^6
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return self.use_list(n, m)

    @classmethod
    def use_list(cls, n, m):
        params = [1 for i in range(n + 1)]

        using = 0  # 现在使用的
        flag = 0  # 计数器 当一个人跳出 则循环置0

        while using < n - 1:
            for i in range(1, n + 1):
                if params[i] == 1:
                    flag += 1
                    if flag == m:
                        using += 1
                        params[i] = 0
                        flag = 0
                if using == n - 1:
                    break
        for index, row in enumerate(params[1:]):
            if row == 1:
                print(f"index : {index}")
                return index
        return -1


if __name__ == "__main__":
    print(Solution().use_list(10, 17))
