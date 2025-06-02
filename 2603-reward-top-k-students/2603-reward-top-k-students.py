import heapq

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # Create a set to map words at O(1)
        positive = set(positive_feedback)
        negative = set(negative_feedback)

        # min heap as we want top k students
        heap = []
    
        for i in range(len(student_id)):
            points = 0
            rep = report[i]
            stud_id = student_id[i]

            for word in rep.split():
                if word in positive:
                    points += 3
                if word in negative:
                    points -= 1

            heapq.heappush(heap, (points, -stud_id))
            # Maintain constraint
            if len(heap) > k:
                heapq.heappop(heap)
        

        heap.sort(reverse=True, key=lambda x: (x[0], x[1]))

        return [-s for _, s in heap]

        
        