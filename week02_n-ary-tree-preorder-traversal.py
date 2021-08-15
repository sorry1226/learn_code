"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # 递归
    def preorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        output = []
        # perform dfs on the root and get the output stack
        self.dfs(root, output)

        return output
    def dfs(self, root, output):

        # 如果根为空直接返回
        if root is None:
            return

        # 前序遍历先输出根节点
        output.append(root.val)

        # 之后输出所有子节点
        for child in root.children:
            self.dfs(child, output)
    # 迭代
    def preorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        # 前序遍历所以先把根节点入栈
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            # 之后依次将下一个遍历到的节点的所有子节点逆序放入堆中
            stack.extend(root.children[::-1])

        return output

