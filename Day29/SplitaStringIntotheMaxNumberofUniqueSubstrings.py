class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        res = [0]
        def dfs(pointer, s):
            # print(visited, pointer,s)
            if len(s)==0 or pointer>=len(s):
                res[0] = max(res[0], len(visited))
                return 
            if s[:pointer+1] in visited:
                return 
            if len(s[:pointer+1])!=0:
                visited.add(s[:pointer+1])
            for x in range(len(s[pointer+1:])+1):
                dfs(x, s[pointer+1:])
            if len(s[:pointer+1])!=0:
                visited.remove(s[:pointer+1])
        pointer = -1 
        dfs(pointer,s)
        return (res[0])