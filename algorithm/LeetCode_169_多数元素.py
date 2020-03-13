"""
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在多数元素。

    示例 1:

    输入: [3,2,3]
    输出: 3
    示例 2:

    输入: [2,2,1,1,1,2,2]
    输出: 2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.use_sort(nums)

    @classmethod
    def use_hash(cls, nums: List[int]) -> int:
        """
            用一个哈希来存储 所有元素 以及对应的出现的次数
            时间复杂度：O(n)
            空间复杂度：O(n)
        """

        mapping = dict()
        half_len = len(nums) // 2

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        for key, value in mapping.items():
            if value > half_len:
                return key

    @classmethod
    def use_sort(cls, nums: List[int]) -> int:
        """
            对目标数据进行排序， 最多元素肯定出现在中间的位置
            时间复杂度：O(nlogn)
            空间复杂度：O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]

    @classmethod
    def use_boyer(cls, nums: List[int]) -> int:
        """
            Boyer-Moore 投票算法
            开始维护一个候选数A 和这个候选数出现的次数， 依次遍历循环。
                分两种情况：
                    1. 和候选数一样 候选次数加1
                    2. 和候选数不一样 候选次数减1，当候选次数等于0时，更改候选数
        """
        candidate_num = None  # 候选数
        candidate_cnt = 0  # 候选次数

        for num in nums:
            if candidate_cnt == 0:
                candidate_num = num
            candidate_cnt += (1 if candidate_num == num else -1)
        return candidate_num
