from collections import defaultdict
import heapq

class UnionFind:
    """Path compression and union by rank"""
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Keep track of the smallest element. This positions the root to 
        be the smallest lexographic element.
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            # Already connected
            return

        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
    


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        We need to find the connected component then find the smallest value in 
        that connected component.
        """
        
        # Need to form a graph
        alpha = "abcdefghijklmnopqrstuvwxyz"
        uf = UnionFind(len(alpha))

        for i in range(len(s1)):
            # Relative positions
            x = ord(s1[i]) - ord('a')
            y = ord(s2[i]) - ord('a')

            uf.union(x, y)

        # now each node in the union find points to the smallest lexographic
        # value the given nodes connected component

        ans = [alpha[uf.find(ord(c) - ord('a'))] for c in baseStr]

        return "".join(ans)