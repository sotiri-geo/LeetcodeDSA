class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        To apply kruskals algo we need to sort the points by weight, which is magnitude
        
        Maybe not optimal but could work O(n2)
        
        1. construct edges between a given node and all other nodes
        2. sort them by weight
        3. apply kruskal algorithm for forming a minimum spanning tree
        4. sum weights of min spanning tree and return
        """
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        # (weight, x1, y1, x2, y2)
        weighted_edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                a = points[i]
                b = points[j]
                # Use indexes instead of coordinates so its easier to apply findUnion
                weighted_edges.append((heuristic(a, b), i, j))
        
        # Sort weights in ascending order
        weighted_edges.sort(key=lambda x: x[0])
        
        # minimum cost is going to be all the weights summed up to n - 1 edges
        # we also need to check for cycles
        # this is where we can optimise with union find algorithm to see if a vertex added
        # creates a cycle
        roots = [i for i in range(n)]
        ranks = [1 for _ in range(n)]
        
        
        def find(x):
            """Path compression to find root of x"""
            if x != roots[x]:
                roots[x] = find(roots[x])
            
            return roots[x]
        
        def union(x, y):
            """Union by Rank to connect two vertices.
            Keeps depth of tree to a minimum.
            Returns True if x and y are not already connected. False otherwise.
            """
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                # already connected
                return False
            
            if ranks[root_x] > ranks[root_y]:
                # join root_y to root_x
                roots[root_y] = root_x
            elif ranks[root_x] < ranks[root_y]:
                # join root_x to root_y
                roots[root_x] = root_y
            else:
                roots[root_y] = root_x
                ranks[root_y] += 1
                
            return True
        
        ans = 0
        count = 0
        # Kruskals algorithm requires us to traverse the weighted edges in asc order
        # and to rejects edges which will create a cycle in our min spanning tree
        # and to have weights of length N - 1
        for w, i, j in weighted_edges:
            
            if union(i, j):
                ans += w
                count += 1
                
            if count == n - 1:
                break
        
        return ans
            
            
            
        
                
        
        
        