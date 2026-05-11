def dfs(i, j, grid, visited):
    r = len(grid)
    c = len(grid[0])

    visited[i][j] = 1

    if i > 0 and grid[i-1][j] == 1 and visited[i-1][j] == 0:
        dfs(i-1, j, grid, visited)

    if i+1 < r and grid[i+1][j] == 1 and visited[i+1][j] == 0:
        dfs(i+1, j, grid, visited)

    if j > 0 and grid[i][j-1] == 1 and visited[i][j-1] == 0:
        dfs(i, j-1, grid, visited)

    if j+1 < c and grid[i][j+1] == 1 and visited[i][j+1] == 0:
        dfs(i, j+1, grid, visited)

def numIslands(grid):
    r = len(grid)
    c = len(grid[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    count = 0
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, grid, visited)
                count += 1
    return count 
if __name__ == "__main__":
    rows, cols = map(int, input().split())
    
    grid = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    
    result = numIslands(grid)
    print(result)
