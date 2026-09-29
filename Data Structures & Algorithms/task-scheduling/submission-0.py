class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        count freq of tasks
        create an empty max heap
        add freq to max heap
        
        create empty q
        set time = 0

        while max heap is not empty
            pop the max
            "decrement" the freq and append to q with the new time it can be added back
            increment time by 1

            if the first in q time == time 
                pop it and add freq back to heap
        
        return time
        """
        freq = Counter(tasks)
        heap = []

        for count in freq.values():
            heapq.heappush(heap, -count)
        
        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                task = heapq.heappop(heap) + 1

                if task:
                    q.append((task, time + n))

            if q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush(heap, count)
        
        return time