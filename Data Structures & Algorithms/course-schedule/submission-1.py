class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap= {i: [] for i in range (numCourses)}
        for courses, pre in prerequisites:
            premap[courses].append(pre)
        visited= set()
        def dfs(currcrs):
            if currcrs in visited:
                return False
            if premap[currcrs] == []:
                return True
            visited.add(currcrs)
            for pre in premap[currcrs]:
                if not dfs(pre):
                    return False
            visited.remove(currcrs)
            premap[currcrs] =[]
            return True
        for crs, pre in prerequisites:
            if not dfs(crs):
                return False
        return True
