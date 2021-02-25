
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# https://leetcode-cn.com/problems/rotate-image/description/
#
# algorithms
# Medium (70.25%)
# Likes:    650
# Dislikes: 0
# Total Accepted:    112.4K
# Total Submissions: 160K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵表示一个图像。
# 
# 将图像顺时针旋转 90 度。
# 
# 说明：
# 
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
# 
# 示例 1:
# 
# 给定 matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# 示例 2:
# 
# 给定 matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#
"""这道题目让我们 in-place，也就说空间复杂度要求 O(1)，如果没有这个限制的话，很简单。
通过观察发现，我们只需要将第 i 行变成第 n - i - 1 列， 因此我们只需要保存一个原有矩阵，然后按照这个规律一个个更新即可。
这道题目让我们 in-place，也就说空间复杂度要求 O(1)，如果没有这个限制的话，很简单。
通过观察发现，我们只需要将第 i 行变成第 n - i - 1 列， 因此我们只需要保存一个原有矩阵，然后按照这个规律一个个更新即可。
这种做法的时间复杂度是 O(n^2) ，空间复杂度是 O(1)
"""
# @lc code=start

from typing import List
# -*- coding:utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        n = h - 1
        for i in range(h//2):
            for j in range(i, n - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = tmp

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    先做矩阵转置（即沿着对角线翻转），然后每个列表翻转；
    :rtype: object
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for m in matrix:
        m.reverse()


class Solution1:

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        通过内置函数zip，可以简单实现矩阵转置，下面的代码等于先整体翻转，后转置；
        不过这种写法的空间复杂度其实是O(n);
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
# @lc code=end
if __name__ == '__main__':
    s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.rotate(matrix))


#复杂度分析
#时间复杂度：O(M * N)O(M∗N)​
#空间复杂度：O(1)O(1)


def rotate3(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    h = len(matrix)
    n = h - 1
    for i in range(h // 2):
        for j in range(i, n - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = tmp
matrix = [[1]]
print(rotate3([[1]]))


def rotate4(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    h = len([[1]])
    n = h - 1
    for i in range(h // 2):
        for j in range(i, n - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = tmp

h = len([[1]])
n = h - 1
for i in range(h // 2):
    for j in range(i, n - i):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[n - j][i]
        matrix[n - j][i] = matrix[n - i][n - j]
        matrix[n - i][n - j] = matrix[j][n - i]
        matrix[j][n - i] = tmp
print(matrix)