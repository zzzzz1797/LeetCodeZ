"""
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

    示例 1:

        输入: 4
        输出: 2

    示例 2:
        输入: 8
        输出: 2
        说明: 8 的平方根是 2.82842...,
             由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        return self.use_mid_query(x)

    @classmethod
    def use_mid_query(cls, x: int) -> int:
        """
            使用二分法

            时间复杂度：O(logn)
            空间复杂度：O(1)
        """
        # 特殊情况处理
        if x in (0, 1):
            return 0

        # 套用二分法模版
        start = 0
        end = x // 2

        while start <= end:
            mid = (start + end) // 2
            target = mid * mid

            if target > x:
                end = mid - 1
            elif target < x:
                start = mid + 1
            else:
                return mid
        return end
