"""
    「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
    1 被读作  "one 1"  ("一个一") , 即 11。
    11 被读作 "two 1s" ("两个一"）, 即 21。
    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

    给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
    注意：整数序列中的每一项将表示为一个字符串。
    示例 1:
        输入: 1
        输出: "1"
        解释：这是一个基本样例。

    示例 2:
        输入: 4
        输出: "1211"
        解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
"""


class Solution:
    """
    1
    2 描述的是1，是一个1，也就是11
    3 描述的是11，是两个1，也就是21
    4 描述的是21，是一个2一个1，也就是12-11
    5 描述的是1211, 是一个1，一个2，两个1，也就是11-12-21
    6 描述的是111221，是三个1，两个2，一个1，也就是31-22-11
    7 描述的是312211，是一个3一个1两个2两个1，也即是13-11-22-21
    以此类推

    """

    def countAndSay(self, n: int) -> str:
        pass

    @classmethod
    def solve_1(cls, n: int) -> str:
        prev_person = "1"

        for i in range(1, n):
            next_person = ""
            num = prev_person[0]
            count = 1

            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person


if __name__ == '__main__':
    
    print(Solution.solve_1(1))
    print(Solution.solve_1(2))
    print(Solution.solve_1(3))