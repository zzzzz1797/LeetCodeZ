"""
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为有效的回文串。

    示例 1:
        输入: "A man, a plan, a canal: Panama"
        输出: true

    示例 2:
        输入: "race a car"
        输出: false
"""
import string


class Solution:
    base_val = string.digits + string.ascii_letters

    def isPalindrome(self, s: str) -> bool:
        start_index = 0
        end_index = len(s) - 1

        while start_index < end_index:
            while s[start_index] not in self.base_val and start_index < end_index:
                start_index += 1

            while s[end_index] not in self.base_val and start_index < end_index:
                end_index -= 1

            if s[start_index].lower() != s[end_index].lower():
                return False
            start_index += 1
            end_index -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
