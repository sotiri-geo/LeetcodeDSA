from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # First build out a graph using a hashmap
        graph = defaultdict(list)
        n = len(isConnected)
        
        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1:
                    graph[u].append(v)
                    # undirected
                    graph[v].append(u)

        # number of provinces is equaivalent to no. of connected components
        seen = set()
        ans = 0

        # dfs
        def dfs(node):
            # check for neighbours
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    # add nei then explore
                    dfs(nei)

        for node in range(n):
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node) # traverses connected component
        
        return ans
            

        

        