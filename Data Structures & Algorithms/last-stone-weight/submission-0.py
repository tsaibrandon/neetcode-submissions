class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        create a heap
        
        loop through the list and append negative value to heap
            pop the top 2
            smash rocks
            add the result back into the heap
        
        return remaining stone or 0 if empty
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            x = -(heapq.heappop(heap))
            y = -(heapq.heappop(heap))

            if x > y:
                heapq.heappush(heap, -(x - y))
            elif x < y:
                heapq.heappush(heap, -(y-x))
            
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0