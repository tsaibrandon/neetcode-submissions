class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        create an adj list for prereq to the course
        create a prereq course count

        put every course with no prereqs into a q
        completed = 0

        while q is not empty:
            pop course from q
            add 1 to completed

            loop through the courses that you can take:
                decrease their prereq count by 1

                if the count == 0:
                    add it to the q
        
        return completed == numCourses
        """

        graph = [[] for _ in range(numCourses)]
        prereq = [0] * numCourses

        for course, req in prerequisites:
            graph[req].append(course)
            prereq[course] += 1

        q = deque()

        for course in range(numCourses):
            if prereq[course] == 0:
                q.append(course)
        
        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for next_course in graph[course]:
                prereq[next_course] -= 1

                if prereq[next_course] == 0:
                    q.append(next_course)
            
        return completed == numCourses
        