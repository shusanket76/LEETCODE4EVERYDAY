from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        # ToDo: Write Your Code Here.
        hasmap = {}
        visited = set()
        for edge in edges:
            if edge[0] in hasmap:
                hasmap[edge[0]].append(edge[1])
            else:
                hasmap[edge[0]] = [edge[1]]
            if edge[1] in hasmap:
                hasmap[edge[1]].append(edge[0])
            else:
                hasmap[edge[1]] = [edge[0]]
        def dfs(adjlist, start, end):

            if start==end:
                return True
            if start in visited:
                return False
            visited.add(start)
            for x in adjlist[start]:
                recr = dfs(adjlist, x, end)
                if recr is True:
                    return True
            return False
        if len(hasmap)!=0:
            return dfs(hasmap, start, end)
        return False

    

