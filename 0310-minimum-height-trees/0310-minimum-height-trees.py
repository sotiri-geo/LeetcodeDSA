from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        undirected_graph = defaultdict(set)
        
        for u, v in edges:
            undirected_graph[u].add(v)
            undirected_graph[v].add(u)
        
        # We essentially need to trim the tree from the leaf nodes
        # these are those with only 1 edge. We should be left with either 
        # 1 or 2 nodes and these are our roots which provide a MST
        
        # init nodes with only 1 edge
        queue = deque([node for node in range(n) if len(undirected_graph[node]) == 1])
        
        remaining_nodes = n
        while remaining_nodes > 2:
            
            leaf_count = len(queue)
            remaining_nodes -= leaf_count 
            
            for _ in range(leaf_count):
                leaf = queue.popleft()
                # should only have one neighbour
                nei = undirected_graph[leaf].pop()
                # remove the pointer to previous leaf
                undirected_graph[nei].remove(leaf)
                if len(undirected_graph[nei]) == 1:
                    # new leaf
                    queue.append(nei)
        
        # should be centroids of tree
        return list(queue)
            
        
        
                
            