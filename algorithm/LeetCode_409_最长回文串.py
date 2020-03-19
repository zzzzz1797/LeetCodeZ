"""
    给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
    在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
    注意:
        假设字符串的长度不会超过 1010。

    示例 1:
        输入:"abccccdd"
        输出: 7

        解释:我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 1. 构建一个列表 用来存储大小写所有字母对应的个数
        letter = [0 for i in range(51)]

        # 2. 循环遍历s将每个字母出现的次数 加上上次出现的次数的和放入到letters
        for s_one in s:
            if s_one >= "a":
                # 说明是小写字母
                s_one_index = ord(s_one) - ord('a')
            else:
                # 说明是大小字母
                s_one_index = ord(s_one) - ord('A') + 26
            letter[s_one_index] += 1

        # 遍历letter 如果下标对应的元素内容不是0，先增加总的出现次数，然后判断这个下标是否是奇数，如果是奇数则对应的奇数个数+1
        res = odd = 0
        for s_one_num in letter:
            if s_one_num != 0:
                res += s_one_num
                if s_one_num % 2 == 1:
                    odd += 1

        if odd == 0:
            # 说明构成的字母全是成对出现的
            return res
        else:
            # 说明有单独的字母剩下来，我们选取其中一个字谜作为中心，其它的单独字母淘汰掉即可
            return res - odd + 1
