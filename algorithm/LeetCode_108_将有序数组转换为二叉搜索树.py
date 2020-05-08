"""
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
        给定有序数组: [-10,-3,0,5,9],
        一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.recursive(nums)

    @classmethod
    def recursive(cls, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left < right:
                mid = (left + right) // 2

                node = TreeNode(nums[mid])
                node.left = helper(left, mid - 1)
                node.right = helper(mid + 1, right)
                return node

        return helper(0, len(nums) - 1)
