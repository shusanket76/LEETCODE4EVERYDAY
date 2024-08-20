class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numberofcities = len(isConnected)
        adjalist = {}
        for x in range(len(isConnected)):
            ele = isConnected[x]
            for y in range(len(ele)):
                if ele[y]==1:
                    if  x+1 in adjalist:
                        adjalist[x+1].append(y+1)
                    else:
                        adjalist[x+1]= [y+1]
        visited = set()
        res = 0 
        def dfs(start, adjlist):
            if start not in visited:
                visited.add(start)
                for y in adjlist[start]:
                    dfs(y, adjlist)
            return 
            
        for x in adjalist:
            if x not in visited:
                dfs(x, adjalist)
                res+=1

        return res