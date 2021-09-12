def maximalSquare(matrix):
    """
    :type: matrix: List[List[str]])
    :rtype: n:int
    """

    if matrix is None or len(matrix) < 1:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0]*(cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1]) + 1
                max_side = max(max_side,dp[i+1][j+1])
    return max_side * max_side


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]


    print(maximalSquare(matrix))

