"""
    冒泡排序
        1、比较相邻的两个元素，如果第一个比第二个大（小）  交换双方。
        2、对每一对元素重复1，直至最后一对。
        3、外层循环控制遍历顺序
    时间复杂度：
        平均：O(n^2)
        最坏：O(n^2)
        最好：O(n)
    空间复杂度：O(1)
    稳定排序
"""
import random
from typing import List


def bubble_sort(data: List[int]) -> List[int]:
    data_len = len(data)

    for i in range(data_len):
        for j in range(data_len - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == '__main__':
    print("=============bubble-sort==========")
    params = list(range(20))
    print(f"ori_params:{params} \n")

    random.shuffle(params)
    print(f"before sort params: {params}\n")
    bubble_sort(params)
    print(f"after sort params: {params}")
