"""
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    示例:
        输入: "25525511135"
        输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        pass

    @classmethod
    def solve_1(cls, s: str) -> List[str]:
        def helper(tmp):
            if not tmp or (len(tmp) > 1 and tmp[0] == '0') or (int(tmp) >= 256):
                return False
            return True

        size = len(s)
        res = []

        for i in range(3):
            for j in range(i + 1, i + 4):
                for z in range(j + 1, j + 4):
                    if size > i and size > j and size > j:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:z + 1]
                        tmp4 = s[z + 1:]

                        if helper(tmp1) and helper(tmp2) and helper(tmp3) and helper(tmp4):
                            res.append(f"{tmp1}.{tmp2}.{tmp3}.{tmp4}")
        return res

    @classmethod
    def dfs(cls, s: str) -> List[str]:
        """
            一共4段代表树的深度一共有四层
        """
        res = []
        size = len(s)
        if size > 12:
            return []

        def helper(index, level, tmp_str):
            if index == size and level == 0:
                res.append(tmp_str[:-1])
                return
            if level == 0:
                return

            for i in range(index, index + 3):
                if size > i:
                    if i == index and s[i] == "0":
                        helper(i + 1, level - 1, tmp_str + s[i] + ".")
                        break
                    elif 0 < int(s[index:i + 1]) < 256:
                        helper(i + 1, level - 1, tmp_str + s[index:i + 1] + ".")

        helper(0, 4, "")
        return res
