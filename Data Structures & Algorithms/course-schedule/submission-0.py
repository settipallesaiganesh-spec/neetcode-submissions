class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        state=[0]*numCourses
        def dfs(course):
            # Found a node already in the current path -> cycle
            if state[course] == 1:
                return False

            # Already processed and no cycle found
            if state[course] == 2:
                return True

            # Mark as currently visiting
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Finished processing this course
            state[course] = 2
            return True

        # Check every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        #Time and space complexity is O(V+E) and O(V+E) respectively