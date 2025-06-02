from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        freq map a -> 2, b -> 1

        Take the most frequent element first

        a -> update freq map 

        We need a way of taking the next most frequent element without 
        taking the last char again.
        """

        ans = []
        heap = [] # max heap

        counter = Counter(s)

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        while heap:
            neg_val, key = heapq.heappop(heap)

            if not ans:
                ans.append(key)
                neg_val += 1
                if neg_val != 0:
                    heapq.heappush(heap, (neg_val, key))
                

            elif ans[-1] != key:
                ans.append(key)
                neg_val += 1
                if neg_val != 0:
                    heapq.heappush(heap, (neg_val, key))
                

            # Two cases here
            # If the popped value is the same as last char we need to look one more time, so buffer value

            elif ans[-1] == key:
                # check for another element in heap
                if heap:
                    next_val, next_key = heapq.heappop(heap)
                    ans.append(next_key)
                    next_val += 1 # neg
                    if next_val != 0:
                        heapq.heappush(heap, (next_val, next_key))
                    # Push back original value without modifying counter
                    heapq.heappush(heap, (neg_val, key))
                else:
                    return ""

        return "".join(ans)



    