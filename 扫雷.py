import random


def minesweeper(m, n, p):
    # m行 n列 p为概率
    matrix = [[0 for col in range(n + 2)] for row in range(m + 2)]
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            ran = random.random()
            if ran > p:
                matrix[row][col] = 0  # 如果ran大于p，说明不是地雷。因为这里的p表示的是地雷的概率。
            else:
                matrix[row][col] = "*"

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if matrix[row][col] == "*":  # 如果这个地方是地雷，就在它周围一圈里的非地雷方格都加1
                for i in range(row - 1, row + 1 + 1):
                    for j in range(col - 1, col + 1 + 1):
                        if matrix[i][j] != "*":  # 只有在该方格不是地雷的时候才会+1
                            matrix[i][j] += 1
    # 打印
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print("*", end=" ") if matrix[i][j] == "*" else print(".", end=" ")
        print()

    print()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(matrix[i][j], end=" ")
        print()
