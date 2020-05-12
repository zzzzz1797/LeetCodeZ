"""
    给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。
    你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。

    样例 1:
        输入: "19:34"
        输出: "19:39"
        解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59 分钟之后。
 
    样例 2:
        输入: "23:59"
        输出: "22:22"
        解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        return self.solve_1(time)

    @classmethod
    def solve_1(cls, time: str) -> str:
        res = cls.time_add_minute(time)
        while not cls.compare_time(time, res):
            res = cls.time_add_minute(res)
        return res

    @classmethod
    def time_add_minute(cls, time: str, target: int = 1) -> str:
        hour, minute = map(int, time.split(":"))
        minute = minute + target
        if minute > 59:
            minute = 0
            hour = hour + 1

            if hour > 23:
                hour = 0

        hour = str(hour) if hour > 9 else f"0{hour}"
        minute = str(minute) if minute > 9 else f"0{minute}"
        return hour + ":" + minute

    @classmethod
    def compare_time(cls, ori_time: str, new_time: str) -> bool:

        for ch in new_time:
            if ch not in ori_time:
                return False
        return True
