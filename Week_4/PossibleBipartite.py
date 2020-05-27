class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = [[] for i in range(N+1)]
        for k in dislikes:
            self.graph[k[0]].append(k[1])
            self.graph[k[1]].append(k[0])
        
        self.colors = [0] * (N+1)
        
        for i in range(1, N+1):
            if self.colors[i] == 0 and not self.dfs(i,1):
                return False
        return True
    
    def dfs(self,vertex,color):
        self.colors[vertex] = color
        for i in self.graph[vertex]:
            if self.colors[i] == color:
                return False
            if self.colors[i] == 0 and not self.dfs(i, -color):
                return False
        return True
        