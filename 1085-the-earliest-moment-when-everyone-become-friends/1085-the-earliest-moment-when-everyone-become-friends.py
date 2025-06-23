class UnionFind:
    
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1 for _ in range(size)]
        self.count = size
        
    def find(self, x):
        """Path compression. LogN"""
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])
        
        return self.roots[x]
    
    def union(self, x, y):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            # both aquatencies so skip
            return 
        
        if self.ranks[root_x] > self.ranks[root_y]:
            self.roots[root_y] = root_x
        elif self.ranks[root_x] < self.ranks[root_y]:
            self.roots[root_x] = root_y
        else:
            self.roots[root_y] = root_x
            self.ranks[root_y] += 1
        
        # Decrement only if we've merged two nodes into the same connected component
        self.count -= 1
        

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
        Sort by timestamp, then we can create a disjoint set data structure
        to union nodes (friends) together. We assume initially everyone has no 
        connected friends and then for each union i.e. connection between nodes
        we decrement the count.
        
        The first time we get to count == 1 then we have the earliest time for which 
        we have a single connected component i.e. everyone is friends.
        """
        
        logs.sort()
        uf = UnionFind(n)
        
        for t, u, v in logs:
            uf.union(u, v)
            if uf.count == 1:
                return t
        
        return -1
        
        
        
        