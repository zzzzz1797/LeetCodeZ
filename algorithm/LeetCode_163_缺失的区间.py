"""
    给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。
    示例：
        输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
        输出: ["2", "4->49", "51->74", "76->99"]
"""
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        pass

    @classmethod
    def solve_1(cls, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        lower = lower - 1
        nums.append(upper + 1)

        for num in nums:
            diff = num - lower

            if diff == 2:
                res.append(str(lower + 1))
            elif diff > 2:
                res.append(str(lower + 1) + "->" + str(num - 1))
            lower = num
        return res


if __name__ == '__main__':
    print(Solution.solve_1([0, 1, 3, 50, 75], 0, 99))
