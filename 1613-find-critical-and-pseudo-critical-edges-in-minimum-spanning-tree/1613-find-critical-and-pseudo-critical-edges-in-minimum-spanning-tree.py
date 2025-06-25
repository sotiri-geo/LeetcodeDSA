from collections import defaultdict

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            # creates a cycle
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_y] += 1
        return True

        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        We need to bucket the equal weights and then skip or backtrack and copy the 
        union find at each branch.

        We need to assess if an edge is critical by removing it and running the MST
        algorithm again to see if the weight of the new MST increases.

        Forcing an edge into an MST is attempting to answer the question, does
        this edge belong in an MST. By first adding it to the MST then running kruskals
        algorithm would still work if it initially belonged in the MST. If the total 
        weight of MST ends up higher than the optimal we can safely ignore it.

        This is exactly the point: 
        we want to check if a valid MST can exist with this edge in it.
        """
        
        # only backtrack on edges with same weight
        edges = [(idx, u, v, w) for idx, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[3])

        def mst(edges, forced_edge: list = None, ignore_edge: list = None):
            count = 0
            mst_cost = 0
            uf = UnionFind(n)
            if forced_edge:
                _, u, v, w = forced_edge
                uf.union(u, v)
                mst_cost += w
                count += 1
            
            for idx, u, v, w in edges:
                if ignore_edge:
                    if idx == ignore_edge[0]:
                        continue
                if uf.union(u, v):
                    count += 1
                    mst_cost += w
                if count == n - 1:
                    break

            if count < n - 1:
                # Disjoint set
                return -1
            return mst_cost

        optimal_mst_cost = mst(edges[:])

        critical = []
        pseudo = []

        for i in range(len(edges)):
            # check if i is critical
            ignore_mst_cost = mst(edges, None, edges[i])
            forced_mst_cost = mst(edges, edges[i], None)
            # critical = removing edge increases MST or disconnects graph
            if ignore_mst_cost == -1 or ignore_mst_cost > optimal_mst_cost:
                critical.append(edges[i][0])
            elif forced_mst_cost == optimal_mst_cost:
                # This will check that we can generate an MST by including the current edge
                pseudo.append(edges[i][0])

        
        return [critical, pseudo]




            
        
        
            