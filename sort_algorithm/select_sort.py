"""
    选择排序
        1、从下标为0到最后选出最小的一个元素和下标为0的元素交换位置
        2、从下标为1到最后选出最小的一个元素和下标为1的元素交换位置
        .......
        n、到最后一个元素停止。
    时间复杂度：
        平均：O(n**2)
        最好：O(n**2)
        最坏：O(n**2)
    空间复杂度：
        O(1)
    不稳定
"""
import random

from typing import List


def select_sort(data: List[int]) -> List[int]:
    data_length = len(data)

    for i in range(data_length):
        min_index = i

        for j in range(i, data_length):
            if data[min_index] > data[j]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    return data


if __name__ == '__main__':
    print("=============insert-sort==========")
    params = list(range(20))
    print(f"ori_params:{params} \n")

    random.shuffle(params)
    print(f"before sort params: {params}\n")
    select_sort(params)
    print(f"after sort params: {params}")
