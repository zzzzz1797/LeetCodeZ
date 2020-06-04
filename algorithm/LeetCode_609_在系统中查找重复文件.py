"""
    给定一个目录信息列表，包括目录路径，以及该目录中的所有包含内容的文件，您需要找到文件系统中的所有重复文件组的路径。
    一组重复的文件至少包括二个具有完全相同内容的文件。
    输入列表中的单个目录信息字符串的格式如下：
        "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
        这意味着有 n 个文件（f1.txt, f2.txt ... fn.txt 的内容分别是 f1_content, f2_content ... fn_content）
        在目录 root/d1/d2/.../dm 下。注意：n>=1 且 m>=0。如果 m=0，则表示该目录是根目录。

    示例 1：
        输入：
            ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
        输出：
            [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]


"""

from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pass

    @classmethod
    def solve_1(cls, paths: List[str]) -> List[List[str]]:
        mapping = {}
        res = []

        for path in paths:
            path_detail = path.split(" ")
            root_path = path_detail[0]
            for path_content in path_detail[1:]:
                content_start_index = path_content.find("(") + 1
                content_end_index = path_content.find(")")
                content = path_content[content_start_index: content_end_index]

                file_path = root_path + "/" + path_content[:content_start_index - 1]
                if content not in mapping:
                    mapping[content] = [file_path]
                else:
                    mapping[content].append(file_path)
        for key, val in mapping.items():
            if len(val) >= 2:
                res.append(val)
        return res


if __name__ == '__main__':
    print(Solution.solve_1(
        ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
