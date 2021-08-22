# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历: 根 左 右
        # 中序遍历: 左 根 右
        if inorder:
            # 前序遍历第一个值为根节点 获取根节点在中序遍历的位置
            ind = inorder.index(preorder.pop(0))
            # 根节点
            root = TreeNode(inorder[ind])
            # 构建左子树
            root.left = self.buildTree(preorder, inorder[0:ind])
            # 构建右子数
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root





