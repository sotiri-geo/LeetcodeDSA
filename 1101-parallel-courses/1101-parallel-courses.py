from collections import deque, defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        We need to adapt kahns algorithm.
        At each step we need to account for a single semester.
        """
        
        # Create graph: directed
        indegree = {node: 0 for node in range(1, n + 1)}
        graph = defaultdict(list)
        
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
            
        # start with the zero dependency nodes
        queue = deque([node for node in range(1, n + 1) if indegree[node] == 0])
        
        order = []
        semesters = 0
        
        while queue:
            
            # We need to exhaust all nodes which have zero indegree at each level
            # this is where we maximise the number of courses which can be taken at each 
            # semester, which leads to the smallest no. semesters required to complete all courses
            
            for _ in range(len(queue)):
            
                node = queue.popleft()
    
                for nei in graph[node]:
                    # reduce in degree on nei
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
                
                order.append(node)
            semesters += 1
                    
        
        # Verify its possibel
        if len(order) == n:
            return semesters
        
        return -1
            
            
            