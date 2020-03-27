"""
    插入排序
        1、从第一个元素开始，该元素可以认为已经被排序。
        2、取出下一个元素，在已经排序的元素序列中从后向前扫描。
        3、如果该元素（已排序）大于新元素，将该元素移到下一位置。
        4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置。
        5、将新元素插入到该位置后。
        6、重复步骤2~5。
    时间复杂度：
        平均：O(n**2)
        最坏：O(n**2)
        最好：O(n)
    空间复杂度：
        O(1)
    稳定排序
"""
import random
from typing import List


def insert_sort(data: List[int]) -> List[int]:
    data_len = len(data)

    for i in range(1, data_len):
        for j in range(i, 0, -1):
            if params[j] < params[j - 1]:
                params[j], params[j - 1] = params[j - 1], params[j]
            else:
                break
    return data


if __name__ == '__main__':
    print("=============insert-sort==========")
    params = list(range(20))
    print(f"ori_params:{params} \n")

    random.shuffle(params)
    print(f"before sort params: {params}\n")
    insert_sort(params)
    print(f"after sort params: {params}")
