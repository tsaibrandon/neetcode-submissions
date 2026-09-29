class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        create an empty min heap

        loop through nums:
            append the num to heap
            if heap len is > k:
                pop the top number from the heap
        
        return top of heap
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]