"""Q8: Matrix Path Optimizer with Dynamic Programming
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
Finds minimum-cost path from top-left to bottom-right moving right/down.
"""
def minimum_path(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be non-empty")
    cols = len(matrix[0])
    if any(len(row) != cols for row in matrix):
        raise ValueError("matrix must be rectangular")
    dp = [[0] * cols for _ in matrix]
    parent = [[None] * cols for _ in matrix]
    dp[0][0] = matrix[0][0]
    for r in range(1, len(matrix)):
        dp[r][0], parent[r][0] = dp[r-1][0] + matrix[r][0], (r-1, 0)
    for c in range(1, cols):
        dp[0][c], parent[0][c] = dp[0][c-1] + matrix[0][c], (0, c-1)
    for r in range(1, len(matrix)):
        for c in range(1, cols):
            prev = (r-1, c) if dp[r-1][c] <= dp[r][c-1] else (r, c-1)
            parent[r][c] = prev
            dp[r][c] = dp[prev[0]][prev[1]] + matrix[r][c]
    path, cell = [], (len(matrix)-1, cols-1)
    while cell is not None:
        path.append(cell)
        cell = parent[cell[0]][cell[1]]
    return dp[-1][-1], list(reversed(path))

if __name__ == "__main__":
    print(minimum_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
