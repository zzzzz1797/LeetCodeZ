"""
    给你一个由 '('、')' 和小写字母组成的字符串 s。
    你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
    请返回任意一个合法字符串。
    有效「括号字符串」应当符合以下 任意一条 要求：
        空字符串或只包含小写字母的字符串
        可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
        可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
    示例 1：
        输入：s = "lee(t(c)o)de)"
        输出："lee(t(c)o)de"
        解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
    示例 2：
        输入：s = "a)b(c)d"
        输出："ab(c)d"
    示例 3：
        输入：s = "))(("
        输出：""
        解释：空字符串也是有效的
    示例 4：
        输入：s = ""(a(b(c)d)""
        输出："a(b(c)d)"
    提示：
        1 <= s.length <= 10^5
        s[i] 可能是 '('、')' 或英文小写字母
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
            思路：
                1、使用两个栈，一个用来相互抵消括号，一个用来存储抵消不了的需要删除的括号，括号里面存的是索引值
                2、遍历需要删除的栈，重新计算新值。
        """
        cancel_stack = []
        remove_stack = []
        for index, row in enumerate(s):
            if row not in ("(", ")"):
                continue
            elif row == "(":
                cancel_stack.append(index)
            elif row == ")":
                cancel_stack.pop() if cancel_stack else remove_stack.append(index)

        remove_stack += cancel_stack

        res = ""
        start_index = -1
        for pop_index in remove_stack:
            while start_index < len(s):
                start_index += 1
                if start_index == pop_index:
                    break
                res += s[start_index]
        return res + s[start_index + 1:]
