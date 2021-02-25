"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(n):
            matrix.append([0 for j in range(n)])

        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = n - 1
        number = 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = number
                number += 1
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = number
                number += 1
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = number
                    number += 1
                rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = number
                    number += 1
                colBegin += 1
        return matrix
