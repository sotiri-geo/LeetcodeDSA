from collections import defaultdict
import heapq

class UnionFind:
    """Path compression and union by rank"""
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            # Already connected
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_y] += 1
    


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        We need to find the connected component then find the smallest value in 
        that connected component.
        """
        
        # Need to form a graph
        alpha = "abcdefghijklmnopqrstuvwxyz"
        uf = UnionFind(len(alpha))

        alpha_map = {s: idx for idx, s in enumerate(alpha)}

        for i in range(len(s1)):
            # connect the nodes to the same parent root
            char1_idx, char2_idx = alpha_map[s1[i]], alpha_map[s2[i]]

            uf.union(char1_idx, char2_idx)
        
        # We now need to sort by each component and get the smallest value
        # Use a heap to manage smallest lexographic element
        root_to_min_heap = defaultdict(list)
        for i in range(len(alpha)):
            char = alpha[i]
            root = uf.find(i)
            heapq.heappush(root_to_min_heap[root], char)

        ans = []

        for c in baseStr:
            root_idx = uf.find(alpha_map[c])
            # First element is smallest
            ans.append(root_to_min_heap[root_idx][0])
        
        return "".join(ans)
        
