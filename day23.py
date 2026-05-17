def dfs(r, c, grid, visited):
    m = len(grid)
    n = len(grid[0])
    visited[r][c] = 1

    if r > 0 and not visited[r-1][c] and grid[r-1][c] == 'O':
        dfs(r-1, c, grid, visited)

    if r+1 < m and not visited[r+1][c] and grid[r+1][c] == 'O':
        dfs(r+1, c, grid, visited)

    if c > 0 and not visited[r][c-1] and grid[r][c-1] == 'O':
        dfs(r, c-1, grid, visited)

    if c+1 < n and not visited[r][c+1] and grid[r][c+1] == 'O':
        dfs(r, c+1, grid, visited)

def surroundO(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]

    for j in range(n):
        if grid[0][j] == 'O' and not visited[0][j]:
            dfs(0, j, grid, visited)
        if grid[m-1][j] == 'O' and not visited[m-1][j]:
            dfs(m-1, j, grid, visited)

    for i in range(1, m-1):
        if grid[i][0] == 'O' and not visited[i][0]:
            dfs(i, 0, grid, visited)
        if grid[i][n-1] == 'O' and not visited[i][n-1]:
            dfs(i, n-1, grid, visited)

    for i in range(1, m-1):
        for j in range(1, n-1):
            if grid[i][j] == 'O' and not visited[i][j]:
                grid[i][j] = 'X'



if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]
    surroundO(grid)
    for row in grid:
        print(''.join(row))
