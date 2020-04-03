"""
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
    例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
    示例 1：
        输入：[3,4,5,1,2]
        输出：1

    示例 2：
        输入：[2,2,2,0,1]
        输出：0
"""

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        start = 0
        end = len(numbers) - 1

        while start <= end:
            mid = (start + end) >> 1

            mid_val = numbers[mid]
            end_val = numbers[end]

            if mid_val > end_val:
                # 如果中间比最后大，则最小的肯定在后面，因为原来是有序的 将头部拆来一部分补到末尾了
                start = mid + 1
            elif mid_val == end_val:
                # 如果等于最后的值，在 [left, mid-1]
                end = end - 1
            else:
                # 最后就是 mid_val < end_val
                end = mid
        return numbers[start]
