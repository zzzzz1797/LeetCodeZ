"""
    归并排序
        1、把长度为n的输入序列分成两个长度为n/2的子序列。
        2、对这两个子序列分别采用归并排序。
        3、将两个排序好的子序列合并成一个最终的排序序列。

    时间复杂度：
        平均：O(nlogn)
        最坏：O(nlogn)
        最好：O(nlogn)
    空间复杂度：
        O(n)
    稳定
"""
import random
from typing import List


def merge_sort_v1(data: List):
    data_length = len(data)

    if data_length <= 1:
        return data

    mid = data_length >> 1  # = data_length // 2
    left_data = merge_sort_v1(data[:mid])
    right_data = merge_sort_v1(data[mid:])
    return merge_v1(left_data, right_data)


def merge_v1(data1: List[int], data2: List[int]) -> List[int]:
    index1 = index2 = 0

    data1_length = len(data1)
    data2_length = len(data2)
    res = []

    while index1 < data1_length and index2 < data2_length:
        if data1[index1] > data2[index2]:
            res.append(data2[index2])
            index2 += 1
        else:
            res.append(data1[index1])
            index1 += 1
    res += data1[index1:]
    res += data2[index2:]
    return res


def merge_sort_v2(data: List):
    return merge_v2(data, [0] * len(data), 0, len(data) - 1)


def merge_v2(data: List, tmp_data: List, left: int, right: int):
    if right <= left:
        return 0
    mid = left + (right - left) // 2
    merge_v2(data, tmp_data, left, mid)
    merge_v2(data, tmp_data, mid + 1, right)

    i = left
    j = mid + 1
    pos = left

    while i <= mid and j <= right:
        if data[i] <= data[j]:
            tmp_data[pos] = data[i]
            i += 1
        else:
            tmp_data[pos] = data[j]
            j += 1
        pos += 1

    for x in range(i, mid + 1):
        tmp_data[pos] = data[x]
        pos += 1

    for y in range(j, right + 1):
        tmp_data[pos] = data[y]
        pos += 1
    data[left:right + 1] = tmp_data[left:right + 1]
    return data


if __name__ == '__main__':
    print("=============merge-sort==========")
    params = list(range(20))
    print(f"ori_params:{params} \n")

    random.shuffle(params)
    print(f"before sort params: {params}\n")
    new_params = merge_sort_v2(params)
    print(f"after sort params: {new_params}")
