class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]
        ones_row = [sum(row) for row in grid]

        ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        for i in range(m):
            for j in range(n):
                ans[i][j] = ones_row[i] + ones_col[j] - (n - ones_row[i]) - (m - ones_col[j])

        return ans