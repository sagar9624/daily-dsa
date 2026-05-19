def dfs(cur, adj, visited, path):
    visited[cur] = True
    path[cur] = True
    for k in adj[cur]:
        if not visited[k]:
            if dfs(k, adj, visited, path):
                return True
        elif path[k]:
            return True
    path[cur] = False
    return False

def cycle(adj, n):
    visited = [False] * n
    path = [False] * n
    for i in range(n):
        if not visited[i]:
            if dfs(i, adj, visited, path):
                return True
    return False

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    
    if cycle(adj, n):
        print(1) 
    else:
        print(0) 

if __name__ == "__main__":
    main()
