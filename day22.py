def dfs(r, c, grid, visited):
    m = len(grid)  # Number of rows
    n = len(grid[0])  # Number of columns
    
    visited[r][c] = 1
    
    if r > 0 and not visited[r - 1][c] and grid[r - 1][c] == 1:
        dfs(r - 1, c, grid, visited)  # Up
    
    if r + 1 < m and not visited[r + 1][c] and grid[r + 1][c] == 1:
        dfs(r + 1, c, grid, visited)  # Down

    if c > 0 and not visited[r][c - 1] and grid[r][c - 1] == 1:
        dfs(r, c - 1, grid, visited)  # Left

    if c + 1 < n and not visited[r][c + 1] and grid[r][c + 1] == 1:
        dfs(r, c + 1, grid, visited)  # Right

def numberOfEnclaves(grid):
    m = len(grid)
    n = len(grid[0])
    
    visited = [[0 for _ in range(n)] for _ in range(m)]
    
    for j in range(n):
        if grid[0][j] == 1 and not visited[0][j]:
            dfs(0, j, grid, visited)
        if grid[m - 1][j] == 1 and not visited[m - 1][j]:
            dfs(m - 1, j, grid, visited)
    for i in range(m):
        if grid[i][0] and not visited[i][0]:
            dfs(i, 0, grid, visited)
        if grid[i][n - 1] and not visited[i][n - 1]:
            dfs(i, n - 1, grid, visited)

    count = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if not visited[i][j] and grid[i][j]:
                count += 1

    return count


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
result = numberOfEnclaves(grid)
print(result)
