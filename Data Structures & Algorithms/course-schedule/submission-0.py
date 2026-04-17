class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range (numCourses)}
        for course, pre in prerequisites:
            premap[course].append(pre)
        visitedcheck= set()
        def dfs(curr):
            if curr in visitedcheck:
                return False
            if premap[curr] == []:
                return True
            visitedcheck.add(curr)
            for pre in premap[curr]:
                if not dfs(pre):
                   return False
            visitedcheck.remove(curr)
            premap[curr]= []
            return True
        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True