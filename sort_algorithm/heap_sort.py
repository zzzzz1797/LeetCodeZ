"""
    堆排序
        堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

        1、将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区。
        2、将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]。
        3、由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆。
        4、然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。
        5、不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

    时间复杂度：
        平均：O(nlogn)
        最坏：O(nlogn)
        最好：O(nlogn)
    空间复杂度：
        O(1)
"""
import random
from typing import List


def heap_sort(data: List):
    data_length = len(data)

    _build_heap(data)  # 构建一个大顶堆

    for i in range(data_length - 1, -1, -1):
        data[i], data[0] = data[0], data[i]
        _hand_heap(data, i, 0)


def _build_heap(data: List):
    data_length = len(data)
    for i in range(data_length // 2, -1, -1):
        _hand_heap(data, data_length, i)


def _hand_heap(data: List, size: int, root_index: int):
    left = 2 * root_index + 1
    right = 2 * root_index + 2
    target_index = root_index

    if left < size and data[left] > data[target_index]:
        target_index = left

    if right < size and data[right] > data[target_index]:
        target_index = right

    if target_index != root_index:
        data[target_index], data[root_index] = data[root_index], data[target_index]
        _hand_heap(data, size, target_index)


if __name__ == '__main__':
    print("=============merge-sort==========")
    params = list(range(20))
    print(f"ori_params:{params} \n")

    random.shuffle(params)
    print(f"before sort params: {params}\n")
    heap_sort(params)
    print(f"after sort params: {params}")
