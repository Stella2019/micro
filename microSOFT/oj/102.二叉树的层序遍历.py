#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.75%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    224.5K
# Total Submissions: 352K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         q, result = [root], []
#         while any(q):
#             tmp = list()
#             len_q = len(q)
#             for _ in range(len_q):
#                 node = q.pop(0)
#                 tmp.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#             result.append(tmp)
#         return result
class Solution:
    def _levelOrder(self, level, result, node):
        if node:
            if level == len(result):
                result.append([])

            result[level].append(node.val)
            self._levelOrder(level + 1, result, node.left)
            self._levelOrder(level + 1, result, node.right)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, result = 0, list()
        self._levelOrder(level, result, root)
        return result


def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]

        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root


def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


if __name__ == "__main__":
    root = [1, None, 2, 3]
    treeRoot = createTree(root)
    printTree(treeRoot)
    print(Solution().levelOrder(treeRoot))


