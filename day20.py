class solution:  affs
    def dfs(self,cur,parent,adj,visited):
        visited[cur]=True 
        for i in adj[cur]:
            if i !=parent:
                if visited[i]:
                    return True 
                elif self.dfs(i,cur,adj,visited):
                    return True 
        return False 
        
    def checkCycle(self,n,adj):
        visited=[False]*n 
        for i in range(n):
            if not visited[i]:
                if self.dfs(i,-1,adj,visited):
                    return True 
        return False 
    

if __name__=="__main__":
  n,e=map(int,input().split()) 
  adj=[[]for _ in range(n)]
  for _ in range(e):
    u,v=map(int,input().split()) 
    adj[u].append(v) 
    adj[v].append(u) 
  print("True" if checkCylce(n,adj) else"False")
