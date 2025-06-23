class UnionFind:
    
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1 for _ in range(size)]
        
    def find(self, x):
        if x != self.roots[x]:
            # Assign it to the root
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        # Theres a cycle if they have the same root and they are both connected
        # with an edge. Draw this out to see it
        if root_x == root_y:
            return False
        
        if self.ranks[root_x] > self.ranks[root_y]:
            self.roots[root_y] = root_x
        elif self.ranks[x] < self.ranks[y]:
            self.roots[root_x] = root_y
        else:
            self.roots[root_x] = root_y
            self.ranks[x] += 1
        
        return True
        
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A child node should only have a single parent. So its invalid if a node 
        has more than one parent
        """
        
        edges_count = len(edges)
        # We require n - 1 to be a valid tree, else there is a cycle or two separate
        # connected components
        if edges_count != n - 1:
            return False
        
            
        uf = UnionFind(n)
        
        for u, v in edges:
            if not uf.union(u, v):
                return False
            
        return True
        