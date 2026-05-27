class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph= defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        print (graph)
        visited=set()
        visiting = set()
        res=[]
        # {1: [0], 
        # 2: [1], 
        # 0: [2]}
        def dfs(pre):
            if pre in visited:
                return True
            if pre in visiting:
                return False
            visiting.add(pre)
            # from the current course, find which courses depend on it
            for course in graph[pre]:
                if not dfs(course):
                    return False
            visited.add(pre)
            visiting.remove(pre)
            res.append(pre)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res[::-1]