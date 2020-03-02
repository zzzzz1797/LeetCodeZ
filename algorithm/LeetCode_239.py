"""
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

    返回滑动窗口中的最大值。
        示例:
            输入:
                nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
            输出:
                [3,3,5,5,6,7]
            解释:
                  滑动窗口的位置                最大值
                ---------------               -----
                [1  3  -1] -3  5  3  6  7       3
                 1 [3  -1  -3] 5  3  6  7       3
                 1  3 [-1  -3  5] 3  6  7       5
                 1  3  -1 [-3  5  3] 6  7       5
                 1  3  -1  -3 [5  3  6] 7       6
                 1  3  -1  -3  5 [3  6  7]      7

    https://leetcode-cn.com/problems/sliding-window-maximum
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.directly(nums, k)

    @classmethod
    def directly(cls, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            max_value = float("-inf")
            for j in range(i, k + i):
                max_value = max(nums[j], max_value)
            res.append(max_value)
            if i == len(nums) - k:
                break
        return res

    @classmethod
    def use_deque(cls, nums: List[int], k: int) -> List[int]:
        """
           nums = [1,3,-1,-3,5,3,6,7], 和 k = 3

            loop1 dq  : [0]
            loop2 dq  :
        """

        dq = deque()
        res = []
        if nums and k <= len(nums):
            for index, element in enumerate(nums):

                while dq and element > nums[dq[-1]]:
                    dq.pop()

                while dq and dq[0] <= index - k:
                    print(index - k, dq[0])
                    # 该元素已经被淘汰了
                    dq.popleft()
            
                dq.append(index)
                if index >= k - 1:
                    res.append(nums[dq[0]])
        return res


if __name__ == '__main__':
    Solution.use_deque([1, 3, -1, -3, 2, 1, 2, 1], 3)
