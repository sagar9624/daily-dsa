def dfs(sr, sc, r, c, v, grid, visited):
    m, n = len(grid), len(grid[0])

    visited[r][c] = 1
    v.append((r-sr, c-sc))

    if r > 0 and grid[r-1][c] and not visited[r-1][c]:
        dfs(sr, sc, r-1, c, v, grid, visited)
    if r+1 < m and grid[r+1][c] and not visited[r+1][c]:
        dfs(sr, sc, r+1, c, v, grid, visited)
    if c > 0 and grid[r][c-1] and not visited[r][c-1]:
        dfs(sr, sc, r, c-1, v, grid, visited)
    if c+1 < n and grid[r][c+1] and not visited[r][c+1]:
        dfs(sr, sc, r, c+1, v, grid, visited)

def distinctIslands(grid):
    m, n = len(grid), len(grid[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    s = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] and not visited[i][j]:
                v = []
                dfs(i, j, i, j, v, grid, visited)
                s.add(tuple(v))
    return len(s)


if __name__ == "__main__":
     rows, cols = map(int, input().split())
     grid = [list(map(int, input().split())) for _ in range(rows)]
     result = distinctIslands(grid)
     print(result)
