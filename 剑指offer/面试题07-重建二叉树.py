"""
    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如，给出
        前序遍历 preorder = [3,9,20,15,7]
        中序遍历 inorder = [9,3,15,20,7]

    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
 
    限制：
        0 <= 节点个数 <= 5000
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        前序遍历  根左右
        中序遍历  左根右
        后续遍历  左右根
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass
