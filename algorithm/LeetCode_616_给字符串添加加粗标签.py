"""
        给一个字符串 s 和一个字符串列表 dict ，你需要将在字符串列表中出现过的 s 的子串添加加粗闭合标签 <b> 和 </b> 。如果两个子串有重叠部分，
    你需要把它们一起用一个闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一个加粗标签包围。

    样例 1：
        输入：
            s = ""abcxyz123""
            dict = ["abc","123"]
        输出：
            "<b>abc</b>xyz<b>123</b>"
    样例 2：
        输入：
            s = "aaabbcc"
            dict = ["aaa","aab","bc"]
        输出：
            "<b>aaabbc</b>c"
"""
from typing import List


class Solution:
    def addBoldTag(self, s: str, dict_: List[str]) -> str:
        # 给dict里面的单词生成对应在s的区间
        section = []
        for word in dict_:
            start_index = s.find(word)
            if start_index != -1:
                section.append([start_index, len(word) - 1 + start_index])

        print(section, "ff")
        # 合并区间
        new_section = []
        for sec in section:
            if not new_section:
                new_section.append(sec)
            else:
                curr_start, curr_end = sec
                last_start, last_end = new_section[-1]
                if last_start <= curr_start <= last_end or curr_start <= last_start <= curr_end or curr_start <= last_end + 1 <= curr_start:
                    new_section[-1] = [min(curr_start, last_start), max(curr_end, last_end)]
                else:
                    new_section.append(sec)
        # 输出结果集
        res = ""
        start = 0
        for curr_start, curr_end in new_section:
            res += s[start:curr_start] + '<b>' + s[curr_start:curr_end + 1] + '</b>'
            start = curr_end + 1
        res += s[start:]
        return res

    def find_sub(self, s, sub_str):
        ret = []
        start_index = s.find(sub_str)
        while start_index >= 0:
            end = start_index + len(sub_str) - 1
            ret.append([start_index, end])
            start_index = s.find(sub_str, start_index + 1)
        return ret

    def addBoldTag1(self, s: str, dict: List[str]) -> str:
        sections = []

        for sub in dict:
            sections.extend(self.find_sub(s, sub))
        sections.sort(key=lambda x: x[0])

        ret_secs = []
        print(sections)
        for section in sections:
            if not ret_secs:
                ret_secs.append(section)
            else:
                if ret_secs[-1][1] < section[0] - 1:
                    ret_secs.append(section)
                else:
                    ret_secs[-1][1] = max(ret_secs[-1][1], section[1])

        print(ret_secs, "pppp")
        ret_s = ''
        sub_start = 0
        for bold_sec in ret_secs:
            ret_s += s[sub_start:bold_sec[0]] + '<b>' + s[bold_sec[0]:bold_sec[1] + 1] + '</b>'
            sub_start = bold_sec[1] + 1
        ret_s += s[sub_start:]
        return ret_s


if __name__ == '__main__':
    # print(Solution().addBoldTag("abcxyz123", ["abc", "123"]))
    # print(Solution().addBoldTag("aaabbcc", ["aaa", "aab", "bc"]))
    # print(Solution().addBoldTag("aaabbcc", ["d"]))
    print(Solution().addBoldTag1("aaabbcc", ["a", "b", "c"]))
    print(Solution().addBoldTag("aaabbcc", ["a", "b", "c"]))
