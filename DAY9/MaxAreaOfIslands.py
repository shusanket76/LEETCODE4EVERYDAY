class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        r = 0
        def dfs(res, x, y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==1 and (x,y) not in visited:
                res[0]+=1
                visited.add((x,y))
                dfs(res,x+1, y)
                dfs(res,x, y-1)
                dfs(res,x, y+1)
                dfs(res,x-1, y)
            return res[0]
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1 and (x,y) not in visited:
                    res = [0]
                    val = dfs(res, x,y)
                    r = max(r, val)
        return r
                    
        