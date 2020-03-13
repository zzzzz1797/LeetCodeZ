"""
    你是一个专业的小偷，计划偷窃沿街的房屋。
    每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

    示例 1:
        输入: [1,2,3,1]
        输出: 4
        解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
             偷窃到的最高金额 = 1 + 3 = 4 。

    示例 2:
        输入: [2,7,9,3,1]
        输出: 12
        解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
             偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.dp_2(nums)

    @classmethod
    def dp_1(cls, nums: List[int]) -> int:
        """
            动态规划：
                dp[i] 表示第i 个房子能偷到的最大值 i从1开始
            状态转移方程:
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            时间复杂度：O(n)
            空间复杂度：O(n)
        """
        res = 0
        if nums:
            nums_len = len(nums)

            # 因为状态转移方程定义的dp[i] 是从1开始所以我们要多加一个元素
            dp = [0] * (nums_len + 1)

            # dp[1] 表示第1间房子能偷到的最大收益，就是第一间房子
            dp[1] = nums[0]

            # 从第二件房子开始循环一只到最后一间房子，所以range的结束要是nums_len+1 这样才会计算到最后一间房子
            for i in range(2, nums_len + 1):
                # 直接套dp公式。这里需要注意的是 i表示的是第几件房子，并不是房子的下标，所以在获取房子的价值时，应该用i-1
                dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
            res = dp[-1]  # 取最后一个
        return res

    @classmethod
    def dp_2(cls, nums: List[int]) -> int:
        """
            动态规划 优化空间复杂度
            状态转移方程还是
                dp[i] = max(dp[i-2] +nums[i], dp[i-1])
            其实每次只需要关系的是dp[i-2] 和dp[i-1]， 用两个变量来代替这两个值，就不用开一维数组了。
            时间复杂度：O(n)
            空间复杂度：O(1)
            这个应该是最优解了，虽然看着不像动态规划，但是用了动态规划的思想。
        """
        prev = 0  # 表示dp[i-2]
        curr = 0  # 表示dp[i-1]
        for num in nums:
            # 用一个临时变量保存dp[i-1]
            tmp_info = curr

            # 下面可以理解成dp[i-1] dp[i-2] 都向前挪了一步

            # 计算判断当前是用dp[i-1] 还是dp[i-2] 并赋值给新的dp[i-1]
            curr = max(prev + num, curr)
            # 将dp[i-1] 赋值给dp[i-2]
            prev = tmp_info

        return curr

    @classmethod
    def recursive(cls, nums: List[int]) -> int:
        """
            从下标为0的房子开始遍历，分为两种情况：
                1） 抢当前的房子 和 抢下下一个房子
                2） 不抢当前的房子， 抢下一个房子
            当房子的下标超出房子的总数时（也包括等于，返回0，即可）
            当房子的下标到达最后一个房子时，只能选择这个房子，因为对于程序来说只剩下这个房子。不存在下一个或者下下一个房子。

            这里用到了lru_cache用做备忘录，缓存已经抢过房子的最大值计算。
            时间复杂度：O(n)
            空间复杂度：O(n)

        """
        nums_len = len(nums)

        @lru_cache(None)
        def helper(index):
            # terminator
            if index == nums_len - 1:
                # 就剩最后一家，那只能抢了
                return nums[index]

            if index >= nums_len:
                # 如果超出门店的个数，返回0 就行
                return 0

            # 当前这家抢，那么就只能抢下下一家 但是可以算上当前这一家的值
            choose_val = helper(index + 2) + nums[index]

            # 当前这一家不抢，那么就抢下一家
            un_choose_val = helper(index + 1)

            # 返回这两种情况的最大值
            return max(choose_val, un_choose_val)

        return helper(0)
