"""
    快速排序
        1、从数列中挑出一个元素，称为 “基准”（pivot）；
        2、重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
        3、把小于基准值元素的子数列和大于基准值元素的子数列排序
    时间复杂度：
        平均：O(logn)
        最坏：O(n**2)
        最好：O(logn)
"""
import random
from typing import List


def quick_sort(data: List[int]) -> None:
    return _quick_sort(data, 0, len(data) - 1)


def _quick_sort(data: List[int], start: int, end: int):
    if start < end:
        pivot = partition(data, start, end)
        _quick_sort(data, start, pivot - 1)
        _quick_sort(data, pivot + 1, end)


def partition(data: List[int], start: int, end: int) -> int:
    index = start - 1
    target = data[end]

    for i in range(start, end):
        if data[i] <= target:
            index += 1
            data[index], data[i] = data[i], data[index]
    data[index + 1], data[end] = data[end], data[index + 1]
    return index + 1


if __name__ == '__main__':
    print("=============quick-sort==========")
    params = list(range(20))
    print(f"ori_params:{params} \n")

    random.shuffle(params)
    print(f"before sort params: {params}\n")
    quick_sort(params)
    print(f"after sort params: {params}")
