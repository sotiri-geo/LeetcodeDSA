from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        Dijkstras algo but instead of looking for the min cost, use max heap
        to always traverse the path where edges contain the highest probability
        Theres also a multiplication step instead of it being additive.
        """
        # graph
        graph = defaultdict(list)

        # No. edges might be less than no. of nodes
        for i in range(len(edges)):
            u, v = edges[i]
            # (node, probability of success)
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])

        probs = [0] * n
        probs[start_node] = 1

        # we have prob of success to reach our start node
        # max heap will need to be negative
        heap = [(-1, start_node)]

        while heap:
            p, node = heapq.heappop(heap)
            
            # check we haven't reached this node before with higher probability
            # if so ignore this path
            if probs[node] > -p:
                continue

            # traverse the graph 
            for neighbour, nei_prob in graph[node]:
                next_prob = -p * nei_prob

                if next_prob > probs[neighbour]:
                    # We've seen better so explore
                    heapq.heappush(heap, (-next_prob, neighbour))
                    probs[neighbour] = next_prob

        return probs[end_node]

            