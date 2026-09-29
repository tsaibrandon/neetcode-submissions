class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        create an empty max heap

        loop through the points and find the distance to origin
            add them to the heap

            if heap len > k:
                remove the farthest point(top of heap)
            
        return heap
        """

        heap = []

        for x, y in points:
            distance = x * x + y * y

            heapq.heappush(heap, (-distance, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for _, x, y in heap]