"""（这是一个 交互式问题 ）
    给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
    如果不存在这样的下标 index，就请返回 -1。
    何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
        首先，A.length >= 3
        其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]
    你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
        MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
        MountainArray.length() - 会返回该数组的长度
"""
from typing import List


class MountainArray:
    def __init__(self, params: List[int]):
        self.params = params

    def get(self, index: int) -> int:
        return self.params[index]

    def length(self) -> int:
        return self.params.__len__()

    def __str__(self):
        return "[" + ",".join(map(str, self.params)) + "]"


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        turning = self.find_turning_pointer_index(mountain_arr)

        print(turning)

        left_min_index = self.find_left_min_index(0, turning, target, mountain_arr)
        if left_min_index != -1:
            return left_min_index

        right_min_index = self.find_right_min_index(turning + 1, mountain_arr.length() - 1, target, mountain_arr)
        if right_min_index != -1:
            return right_min_index
        return -1

    @classmethod
    def find_left_min_index(cls, start, end, target, mountain_arr: MountainArray) -> int:
        res = -1

        print(start, end, mountain_arr)
        while start < end:
            mid = (start + end) // 2
            if mountain_arr.get(mid) > target:
                start = mid + 1
            else:
                end = mid

        if mountain_arr.get(start) == target:
            res = start
        return res

    @classmethod
    def find_right_min_index(cls, start, end, target, mountain_arr: MountainArray) -> int:
        res = -1
        while start < end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) > target:
                start = mid + 1
            else:
                end = mid

        if mountain_arr.get(start) == target:
            res = start
        return res

    @classmethod
    def find_turning_pointer_index(cls, mountain_arr: MountainArray) -> int:
        start = 0
        end = mountain_arr.length() - 1
        while start < end:
            mid = (start + end) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                start = mid + 1
            else:
                end = mid
        return start
