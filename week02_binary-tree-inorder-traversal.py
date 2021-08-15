# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 用True及False来标记节点是否被遍历过
        res = []
        stack = [(root,False)]
        while stack:
            cur, visted = stack.pop()
            if cur is None:
                continue
            # 如果节点被遍历过则输出, 否则(由于是中序遍历)按照 右 自身 左的顺序依次将节点入栈
            if visted:
                res.append(cur.val)
            else:
                stack.append((cur.right,False))
                stack.append((cur,True))
                stack.append((cur.left,False))
        return res