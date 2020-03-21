"""
    输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
    示例 1：
        输入：arr = [3,2,1], k = 2
        输出：[1,2] 或者 [2,1]
    示例 2：
        输入：arr = [0,1,2,1], k = 1
        输出：[0]
    限制：

    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000
"""
import random
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return self.quick_select(arr, k)

    @classmethod
    def use_sort(cls, arr: List[int], k: int) -> List[int]:
        """
            使用python的sort,对列表进行排序。
            时间复杂度：O(nlogn)
            空间复杂度：O(n)
            python 排序的内部实现原理：https://www.cnblogs.com/clement-jiao/p/9243066.html
        """
        arr.sort()
        return arr[:k]

    @classmethod
    def quick_select(cls, arr: List[int], k: int) -> List[int]:
        def partition(nums: List[int], left_index: int, right_index: int) -> int:
            pivot = nums[right_index]
            index = left_index - 1

            for tmp_index in range(left_index, right_index):
                if nums[tmp_index] <= pivot:
                    index += 1
                    nums[index], nums[tmp_index] = nums[tmp_index], nums[index]
            nums[index + 1], nums[right_index] = nums[right_index], nums[index + 1]
            return index + 1

        def random_partition(nums: List[int], left_index: int, right_index: int):
            index = random.randint(left_index, right_index)
            nums[right_index], nums[index] = nums[index], nums[right_index]
            return partition(nums, left_index, right_index)

        def random_selected(nums: List[int], left_index: int, right_index: int, target: int):
            pos = random_partition(nums, left_index, right_index)
            num = pos - left_index + 1

            if target < num:
                random_selected(nums, left_index, pos - 1, k)
            elif target > num:
                random_selected(nums, pos + 1, right_index, target - num)

        if k:
            random_selected(arr, 0, len(arr) - 1, k)

            return arr[:k]
        return []
