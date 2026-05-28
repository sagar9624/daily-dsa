def dfs(curr, adj, visited, path, ans):
    visited[curr] = 1
    path[curr] = 1
    afag
    for k in adj[curr]:
        if not visited[k]:
            if dfs(k, adj, visited, path, ans):
                return True
        elif path[k]:
            return True
            
    path[curr] = 0
    ans.append(curr)
    return False

def safeNodes(adj):
    n = len(adj)
    visited = [0] * n
    path = [0] * n
    ans = []
    
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited, path, ans)
    
    ans.sort()
    return ans


if __name__ == "__main__":
    n, e = map(int, input().split())

    adj = [[] for _ in range(n)]

    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)

    result = safeNodes(adj)
    
    if len(result) == 0:
        print("[]")
    else:
        for i in result:
            print(i, end=" ")
