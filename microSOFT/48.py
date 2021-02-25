matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
h = len(matrix)
n = h - 1
for i in range(h // 2):
    for j in range(i, n - i):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[n - j][i]
        matrix[n - j][i] = matrix[n - i][n - j]
        matrix[n - i][n - j] = matrix[j][n - i]
        matrix[j][n - i] = tmp
print(matrix)