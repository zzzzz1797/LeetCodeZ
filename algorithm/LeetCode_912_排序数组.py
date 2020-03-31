"""
给你一个整数数组 nums，将该数组升序排列。
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bubble_sort(nums)

    @classmethod
    def bubble_sort(cls, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    @classmethod
    def select_sort(cls, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    @classmethod
    def insert_sort(cls, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break
        return nums

    @classmethod
    def quick_sort(cls, nums: List[int]) -> List[int]:
        def _quick_sort(params, start, end):
            if start <= end:
                pivot = partition(params, start, end)
                _quick_sort(params, start, pivot - 1)
                _quick_sort(params, pivot + 1, end)

        def partition(params, start, end):
            index = start - 1
            target = params[end]

            for i in range(start, end):
                if params[i] <= target:
                    index += 1
                    params[index], params[i] = params[i], params[index]
            params[index + 1], params[end] = params[end], params[index + 1]
            return index + 1

        _quick_sort(nums, 0, len(nums) - 1)
        return nums

    @classmethod
    def merge_sort(cls, nums: List[int]) -> List[int]:
        def _merge_sort(data):
            if len(data) < 2:
                return data
            mid_index = len(data) >> 1
            left_data = _merge_sort(data[:mid_index])
            right_data = _merge_sort(data[mid_index:])
            return _merge(left_data, right_data)

        def _merge(data1, data2):
            res = []
            index1 = index2 = 0
            while index1 < len(data1) and index2 < len(data2):
                if data1[index1] < data2[index2]:
                    res.append(data1[index1])
                    index1 += 1
                else:
                    res.append(data2[index2])
                    index2 += 1
            res += data1[index1:]
            res += data2[index2:]
            return res

        return _merge_sort(nums)

    @classmethod
    def heap_sort(cls, nums: List[int]) -> List[int]:
        def build_heap(data):
            data_length = len(data)
            for i in range(data_length // 2, -1, -1):
                hand_heap(data, data_length, i)

        def hand_heap(data, size, index):
            target = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and data[left] > data[target]:
                target = left

            if right < size and data[right] > data[target]:
                target = right

            if target != index:
                data[index], data[target] = data[target], data[index]
                hand_heap(data, size, target)

        build_heap(nums)

        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            hand_heap(nums, i, 0)
        return nums


if __name__ == '__main__':
    print(Solution.bubble_sort([5, 2, 3, 1]))
