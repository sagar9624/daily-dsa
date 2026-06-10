from collections import 

def rottenOranges(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    q = deque()
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                q.append(((i, j), 0))
                visited[i][j] = 1
                
    ans_t = 0
    while q:
        (r, c), t = q.popleft()
        ans_t = max(ans_t, t)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 1 and not visited[nr][nc]:
                q.append(((nr, nc), t+1))
                visited[nr][nc] = 1
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                return -1  
                
    return ans_t


if __name__ == "__main__":
    # Dynamic input
    m, n = map(int, input().split())
    matrix = []

    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = rottenOranges(matrix)
    print(result)
