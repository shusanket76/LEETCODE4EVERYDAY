class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        hasmap = {}
        for x in range(len(isConnected)):
            ele = isConnected[x]
            hasmap[x+1] = []
            for y in range(len(ele)):
                if ele[y]==1 and x!=y:
                    key = x+1
                    
                    hasmap[key].append(y+1)
        
        def dfs(hasmap, x):
            if x not in visited:
                visited.add(x)
                for y in hasmap[x]:
                    dfs(hasmap, y)
            
        res = 0
        visited = set()
        for x in hasmap:
            if x not in visited:
                res+=1
                dfs(hasmap, x)
                    
        return (res)

        