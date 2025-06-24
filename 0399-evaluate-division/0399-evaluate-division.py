class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Keep track of parent (maps a node to its parent)
        and weight (x / parent[x] = weight[x])
        i.e if a / b = 2 then b is a parent of a as we have a -> b has weight 2
        so weight[x] = x / parent[x]

        This solution attempts to find all the weights of x & y to compute
        weight[x] / weight[y]
        """

        parent = {}
        weight = {}

        def find(x):
            """
            x points to root
            weight[x] = x / root
            """
            if parent[x] != x:
                orig_parent = parent[x]
                # update across chain
                parent[x] = find(parent[x])
                # a = 2 * b = 2 * (3 * c) = 6 * c 
                # we multiply the weights across the chain
                # so we get a / c = 6 i.e. x / root[x] = 6
                weight[x] *= weight[orig_parent]
            return parent[x]

        def union(x, y, val):
            # start with weight 1
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
            if y not in parent:
                parent[y] = y
                weight[y] = 1.0

            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                # update two roots to merge together
                # we pick the parent here to be root_x
                parent[root_x] = root_y
                weight[root_x] = val * weight[y] / weight[x]

        def is_connected(x, y):
            if x not in parent or y not in parent:
                return -1.0
            
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                # not connected
                return -1.0
            return weight[x] / weight[y]

        for (x, y), val in zip(equations, values):
            union(x, y, val)

        ans = []

        for x, y in queries:
            ans.append(is_connected(x, y))

        return ans
            

        
