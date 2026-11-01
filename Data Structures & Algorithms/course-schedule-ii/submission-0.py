class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            prereqs[crs].append(prereq)

        order = []
        valid, visited = set(), set()
        def dfs(crs: int) -> bool:
            if crs in visited: return False
            if crs in valid: return True

            visited.add(crs)
            for prereq in prereqs[crs]:
                if not dfs(prereq): return False

            visited.remove(crs)
            valid.add(crs)
            order.append(crs)

            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return []

        return order


