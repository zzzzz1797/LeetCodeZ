"""
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，
采取相反方式重构得到原数据。

    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这
个字符串反序列化为原始的树结构。

    示例: 
        你可以将以下二叉树：
            1
           / \
          2   3
             / \
            4   5
    序列化为 "[1,2,3,null,null,4,5]"
    提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
    说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def helper(node):
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                helper(node.left)
                helper(node.right)

        helper(root)
        return "[" + ",".join(map(str, res)) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(nodes):
            if nodes[0] is None:
                nodes.pop(0)
                return
            root = TreeNode(nodes[0])
            nodes.pop(0)
            root.left = helper(nodes)
            root.right = helper(nodes)
            return root

        return helper(data.split(","))
