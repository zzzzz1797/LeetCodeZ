"""
    给你一个整数数组arr和一个目标值target，请你返回一个整数value，使得将数组中所有大于value的值变成value后，数组的和最接近target
（最接近表示两者之差的绝对值最小）。
    如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
    请注意，答案不一定是 arr 中的数字
"""
import bisect
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        pass

    @classmethod
    def solve_1(cls, arr: List[int], target: int) -> int:
        arr.sort()

        size = len(arr)

        # 求前缀和
        prefix_sum = [0]
        for num in arr:
            prefix_sum.append(prefix_sum[-1] + num)

        right = max(arr)
        res = 0
        diff = target

        for index in range(1, right + 1):
            tmp_index = bisect.bisect_left(arr, index)
            cur_res = prefix_sum[tmp_index] + (size - tmp_index) * index
            if abs(cur_res - target) < diff:
                res, diff = index, abs(cur_res - target)

        return res

    @classmethod
    def solve_2(cls, arr: List[int], target: int) -> int:
        """
        https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/wu-xu-pai-xu-he-er-fen-you-hua-bao-li-fa-by-tinyli/
        :param arr:
        :param target:
        :return:
        """
        total = sum(arr)
        if total <= target:
            return total

        size = len(arr)
        val = target // size
        total, last_info = val * size, 0

        while total < target:
            last_info, total = total, 0

            for i in range(size):
                total += arr[i] if val > arr[i] else val
            val += 1
        return val - 2 if abs(target - total) >= abs(target - last_info) else val - 1
