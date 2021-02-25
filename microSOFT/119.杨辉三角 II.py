"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] + [0] * rowIndex
        for i in range(rowIndex):
            result[0] = 1
            for j in range(i + 1, 0, -1):
                result[j] = result[j] + result[j - 1]

        return result