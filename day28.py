from collections import deque

def dfs(cur, adj, visited, s):
    visited[cur] = True
    for k in adj[cur]:
        if not visited[k]:
            dfs(k, adj, visited, s)
    s.append(cur)

def topologicalSort(adj):
    n = len(adj)
    visited = [False] * n
    s = deque()
    
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited, s)
    
    ans = []
    while s:
        ans.append(s.pop())
    return ans

if __name__ == "__main__":
    n, e = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
    res = topologicalSort(adj)
    print(" ".join(map(str, res)))
