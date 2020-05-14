"""
    Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。
        addRange(int left, int right) 添加半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
        queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true。
        removeRange(int left, int right) 停止跟踪区间 [left, right) 中当前正在跟踪的每个实数。

    示例：
        addRange(10, 20): null
        removeRange(14, 16): null
        queryRange(10, 14): true （区间 [10, 14) 中的每个数都正在被跟踪）
        queryRange(13, 15): false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
        queryRange(16, 17): true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
    提示：
        半开区间 [left, right) 表示所有满足 left <= x < right 的实数。
        对 addRange, queryRange, removeRange 的所有调用中 0 < left < right < 10^9。
        在单个测试用例中，对 addRange 的调用总数不超过 1000 次。
        在单个测试用例中，对  queryRange 的调用总数不超过 5000 次。
        在单个测试用例中，对 removeRange 的调用总数不超过 1000 次。
"""
from typing import List


class RangeModule:

    def __init__(self):
        self.range = []

    def addRange(self, left: int, right: int) -> None:
        tmp_range = []

        if self.range:

            for index, row in enumerate(self.range):
                if not tmp_range:
                    tmp_range.append(row)
                else:
                    if self.check_range_can_merge(tmp_range[-1], row):
                        tmp_range[-1] = self.merge_range(tmp_range[-1], row)
                    else:
                        tmp_range.append(row)

                if left is not None and right is not None:
                    if self.check_range_can_merge(tmp_range[-1], [left, right]):
                        tmp_range[-1] = self.merge_range(tmp_range[-1], [left, right])
                        left = right = None
                    else:
                        if right < tmp_range[-1][0]:
                            #  说明这个空间比现有的最后一个空间还小
                            tmp_info = tmp_range[-1]
                            tmp_range[-1] = [left, right]
                            tmp_range.append(tmp_info)
                            left = right = None

        self.range = tmp_range + [[left, right]] if left is not None else tmp_range

    def queryRange(self, left: int, right: int) -> bool:
        for curr_left, curr_right in self.range:
            if curr_left <= left < curr_right and curr_left < right <= curr_right:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        tmp_range = []
        target = [left, right]
        for index, row in enumerate(self.range):
            curr_left, curr_right = row
            if self.check_range_can_merge(target, row):
                # 1. 判断现在当前这个区间是不是完全包含在需要删除的区间内，如果是就删除当前这个区间
                if self.check_range_is_contain(target, row):
                    continue
                # 2.  如果条件1 不满足，那么肯定是当前这个区间包含现在需要删除的区间，将当前这个区间根据需要删除的区间进行切分

                if curr_left < left:
                    tmp_range.append([curr_left, left])
                if right < curr_right:
                    tmp_range.append([right, curr_right])

            else:
                tmp_range.append([curr_left, curr_right])

        new_range = []
        for index, row in enumerate(tmp_range):
            if not new_range:
                new_range.append(row)
            else:
                if self.check_range_can_merge(new_range[-1], row):
                    new_range[-1] = self.merge_range(new_range[-1], row)
                else:
                    new_range.append(row)
        self.range = new_range

    @classmethod
    def check_range_is_contain(cls, range_1, range_2) -> bool:
        """
            检查range1 是否包含range2
        """
        left_1, right_1 = range_1
        left_2, right_2 = range_2
        if left_1 <= left_2 and right_1 >= right_2:
            return True
        return False

    @classmethod
    def check_range_can_merge(cls, range_1, range_2) -> bool:
        """
            检查range1 和 range2是否可以合并
        """
        left_1, right_1 = range_1
        left_2, right_2 = range_2
        if left_1 <= left_2 <= right_1 or left_2 <= left_1 <= right_2:
            return True
        return False

    @classmethod
    def merge_range(cls, range_1, range_2) -> List[int]:
        """
            合并两个 可以合并的区间
        """
        assert cls.check_range_can_merge(range_1, range_2)
        left_1, right_1 = range_1
        left_2, right_2 = range_2
        return [min(left_1, left_2), max(right_1, right_2)]
