"""
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

    示例 1:
        输入: "Let's take LeetCode contest"
        输出: "s'teL ekat edoCteeL tsetnoc" 
    注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        size = len(s)
        start_index = 0
        last_index = 0

        res = ""

        while start_index <= size - 1:
            if s[start_index] == " ":
                res += self.swap_word(s[last_index:start_index]) + " "
                while s[start_index] == " ":
                    start_index += 1
                last_index = start_index
            start_index += 1
        return res + self.swap_word(s[last_index:start_index])

    @classmethod
    def swap_word(cls, word):
        end = len(word) - 1

        res = ""
        while end >= 0:
            res += word[end]
            end -= 1
        return res


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))
