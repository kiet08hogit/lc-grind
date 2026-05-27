class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # {0: [1], 
        # 1: [0, 2], 
        # 2: [1], 
        # 3: [4], 
        # 4: [3]
        visited=set()
        count=0 
        def dfs(curr):
            if curr not in visited:
                visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor in visited: 
                    continue
                else:
                    dfs(neighbor)
        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node)
        return count