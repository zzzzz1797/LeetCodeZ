"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        a_size = len(a)
        b_size = len(b)

        a_index = a_size - 1
        b_index = b_size - 1

        while a_index >= 0 or b_index >= 0:
            a_val = int(a[a_index]) if a_index >= 0 else 0
            b_val = int(b[b_index]) if b_index >= 0 else 0

            tmp_val = a_val + b_val + carry
            print(a_val, b_val, carry)
            new_val = tmp_val % 2
            carry = tmp_val // 2

            res.append(new_val)
            if a_index >= 0:
                a_index -= 1
            if b_index >= 0:
                b_index -= 1

        if carry:
            res.append(carry)
        res = reversed(list(map(str, res)))
        return "".join(res)


if __name__ == '__main__':
    print(Solution().addBinary("111", "1"))
