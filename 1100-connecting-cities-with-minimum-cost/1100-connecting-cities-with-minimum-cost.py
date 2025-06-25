from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        Using prims algorithm to create minimum spanning tree.

        We essentially need to visit each node and then take all of its edges
        and add to the min heap. We then greedily select the edge with lowest weight 
        and explore that. If the node the edge connects hasn't been seen, we add this
        to the min spanning tree set and increment total mst_cost. We skip those edges
        which connect to nodes we have already seen.

        In the event we have a disjoint set of nodes, we return -1
        """

        # create a graph
        graph = defaultdict(list)

        for u, v, w in connections:
            graph[u].append((w, v))
            graph[v].append((w, u)) # undirected

        visited = set()
        # (weight, node)
        min_heap = [(0, 1)] # start at city 1 (not important)
        mst_cost = 0

        while len(visited) < n and min_heap:
            weight, city = heapq.heappop(min_heap)

            if city in visited:
                continue
            
            visited.add(city)
            mst_cost += weight

            # explore all edges of this node
            for edge_weight, nei in graph[city]:
                if nei not in visited:
                    heapq.heappush(min_heap, (edge_weight, nei))
        
        return mst_cost if len(visited) == n else -1
