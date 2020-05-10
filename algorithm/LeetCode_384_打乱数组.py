"""
    打乱一个没有重复元素的数组。
    示例:
        // 以数字集合 1, 2 和 3 初始化数组。
        int[] nums = {1,2,3};
        Solution solution = new Solution(nums);

        // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
        solution.shuffle();

        // 重设数组到它的初始状态[1,2,3]。
        solution.reset();

        // 随机返回数组[1,2,3]打乱后的结果。
        solution.shuffle();
"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.ori_nums = nums
        self.size = len(nums)
        self.new_nums = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.ori_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(0, self.size):
            new_index = random.randrange(i, self.size)
            self.new_nums[new_index], self.new_nums[i] = self.new_nums[i], self.new_nums[new_index]
        return self.new_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    print(Solution([1, 2, 3, 4]).shuffle())
