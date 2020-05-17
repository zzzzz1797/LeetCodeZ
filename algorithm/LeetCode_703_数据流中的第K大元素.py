import heapq
from typing import List


class KthLargest:
    """
        构建一个小顶堆

    """

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.length = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.length:
            heapq.heappush(self.nums, val)
        else:
            if val > self.nums[0]:
                heapq.heapreplace(self.nums, val)
        return self.nums[0]
