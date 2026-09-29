class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        create an adj list
        create a prereq list 

        loop through the prerequisites
            add prereq to the corresponding course
            increase prereq count by 1

        put every course with no prereqs into a q
        create result list 

        while q is not empty:
            pop the left course from q 
            add it to the result 

            for every course that now can be taken:
                decrease its prereq by 1
                if the prereq count == 0:
                    add it to the q

        if the result contains all courses:
            return the result
        else:
            return []
        """
        graph = [[] for _ in range(numCourses)]
        req = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            req[crs] += 1
        
        q = deque()

        for crs in range(numCourses):
            if req[crs] == 0:
                q.append(crs)
        
        res = []

        while q:
            crs = q.popleft()
            res.append(crs)

            for nxt in graph[crs]:
                req[nxt] -= 1

                if req[nxt] == 0:
                    q.append(nxt)
        
        if len(res) == numCourses:
            return res
        
        return []