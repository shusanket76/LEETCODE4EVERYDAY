class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        visited2 = set()
        res = [0]

        def dfs(x, y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in visited and grid[x][y]==0:
                visited.add((x,y))
                grid[x][y]=-2
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x+1,y)
                dfs(x,y+1)
        def countisland(x,y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in visited2 and grid[x][y]==0:
                visited2.add((x,y))
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x+1,y)
                dfs(x,y+1)
                return True
            else:
                return False
            
        
        # check all rows
        for x in range(len(grid)):
            # first element of every row
            if grid[x][0]==0:
                dfs(x, 0)
            
            # last element of every row
            if grid[x][len(grid[0])-1]==0:
                dfs(x, len(grid[0])-1)
        
        for y in range(len(grid[0])):

            # check first column 

            if grid[0][y]==0:
                dfs(0,y)

            # check last col 
            if grid[len(grid)-1][y]==0:
                dfs(len(grid)-1, y)
        # print(grid)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==0:
                    count = countisland(x,y)
                    if count is True:
                        res[0]+=1
        return (res[0])

            