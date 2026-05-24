class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # graph = {
        #     0: [1],
        #     1: [0, 2, 3,4],
        #     2: [1,3],
        #     3: [1,2],
        #     4: [1]
        # }
        visited= set()
        # (0,-1)
        def dfs (curr,parent):
            if curr not in visited:
                visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                else:
                    if dfs(neighbor, curr) == False:
                        return False
                    dfs(neighbor,curr)
            return True
        
        return dfs(0,-1) and  len(visited) == n
    
