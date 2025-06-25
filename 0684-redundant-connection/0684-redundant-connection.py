class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.parent[x]:
            # Update x to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            # Found our cycle
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        We need to efficiently find the edge which causes the graph to be a cycle then 
        return it.

        Using kruskals algorithm with a unionFind datastructure to efficiently find this edge.

        Nodes are labelled from 1 to N hence we need to factor in that our array is 0 indexed.
        """
        nodes = set()

        for u, v in edges:
            nodes.add(u - 1)
            nodes.add(v - 1)
        
        n = len(nodes)        

        def redundantEdge(n, edges):
            """Returns the edge which forms a cycle. If multiple returns last."""
            uf = UnionFind(n)

            cycle_edges = []
            # we need to start from the first edge in list
            # there should only be one element in the cycle edges

            for u, v in edges:
                # 0 index
                if not uf.union(u - 1, v - 1):
                    cycle_edges.append((u, v))

            return cycle_edges.pop()

        return redundantEdge(n, edges)

