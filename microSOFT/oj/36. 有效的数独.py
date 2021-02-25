"""class Solution:
# 全局变量，存储每行、每列和每个block当中放置的数字的数量
# 用数组会比dict更快
    rowDict = [[0 for _ in range(10)] for _ in range(10)]
    colDict = [[0 for _ in range(10)] for _ in range(10)]
    blockDict = [[0 for _ in range(10)] for _ in range(10)]

    def dfs(self, cur, bd, board):
        if cur == 81:
        # 拼装答案
            for i in range(9):
                for j in range(9):
                    board[i][j] = chr(ord('0') + bd[i][j])
            return

        x, y = cur // 9, cur % 9 # 如果原本就有数字，直接跳过
        if bd[x][y] != 0:
            self.dfs(cur+1, bd, board)
            return
        for i in range(1, 10):# 如果在行或者列或者block中出现过，那么当下不能放入
            blockId = (x // 3) * 3 + y // 3
            if Solution.rowDict[x][i] > 0 or Solution.colDict[y][i] > 0:
                continue
            # 更新容器
            bd[x][y] = i
            Solution.rowDict[x][i] += 1
            Solution.colDict[y][i] += 1
            Solution.blockDict[blockId][i] += 1
            # 往下递归
            self.dfs(cur+1, bd, board)
            # 回溯之后还原
            bd[x][y] = 0
            Solution.rowDict[x][i] -= 1
            Solution.colDict[y][i] -= 1
            Solution.blockDict[blockId][i] -= 1


    def solveSudoku(self, board: List[List[str]]) -> None:
 #Do not return anything, modify board in-place instead.
        bd = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):

            for j in range(9):

                if board[i][j] != '.':
# 将字符串转成数字
                bd[i][j] = ord(board[i][j]) - ord('0')
# 将已经填好的数字插入我们的容器当中
                Solution.rowDict[i][bd[i][j]] += 1
                Solution.colDict[j][bd[i][j]] += 1
# 计算一下在哪个block当中
                blockId = (i // 3) * 3 + j // 3
                Solution.blockDict[blockId][bd[i][j]] += 1
        self.dfs(0, bd, board)
 """


class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cacheCol = [[0] * 9 for _ in xrange(0, 10)]
        cacheRow = [[0] * 9 for _ in xrange(0, 10)]
        cacheBox = [[0] * 9 for _ in xrange(0, 10)]

        for i in xrange(0, 9):
            for j in xrange(0, 9):
                ib = (i / 3) * 3 + j / 3
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                if cacheRow[i][num] != 0 or cacheCol[j][num] != 0 or cacheBox[ib][num] != 0:
                    return False
                cacheRow[i][num] = 1
                cacheCol[j][num] = 1
                cacheBox[ib][num] = 1
        return True


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []

        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit != '.':
                    seen.append((i, digit))
                    seen.append((digit, j))
                    seen.append((i // 3, j // 3, digit))

        return len(seen) == len(set(seen))


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    result = Solution().isValidSudoku(board)
    print(board)
    print(result)