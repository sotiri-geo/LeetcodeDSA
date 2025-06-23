from collections import defaultdict
import heapq 

class UnionFind:
    
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1 for _ in range(size)]
        
    def find(self, x):
        """Path compression"""
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
            
    
    def union(self, x, y):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        # ignore if they have same root
        if root_x == root_y:
            return 
        
        if self.ranks[root_x] > self.ranks[root_y]:
            self.roots[root_y] = root_x
        elif self.ranks[root_x] < self.ranks[root_y]:
            self.roots[root_x] = root_y
        else:
            self.roots[root_y] = root_x
            self.ranks[root_y] += 1
            
        
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        If we can group the connected components together, we need to pick the union based
        on the smallest lexographical order.
        """
        
        ans = []
        
        uf = UnionFind(len(s))
        
        for u, v in pairs:
            uf.union(u, v)
            
        components = defaultdict(list)
        # Push components onto heap
        for i in range(len(s)):
            # use find() to guarentee finding root for index i
            root = uf.find(i)
            heapq.heappush(components[root], s[i])
        
        # Now reconstruct the answer by finding the root which is key
        # for the connected components that the index of s lives
        # we pop from heap to find the min element at O(LogK) time
        # Where K is the average size of the connected component
        
        for i in range(len(s)):
            root = uf.find(i)
            conn_component = components[root]
            ans.append(heapq.heappop(conn_component))
            
        return "".join(ans)
        
            
        
        
        
        