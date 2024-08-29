class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x, y, visited, pointer=0):
            if pointer==len(word):
                return True
            if x>=0 and y>=0 and x<len(board) and y<len(board[0]) and (x,y) not in visited and board[x][y]==word[pointer]:

                visited.add((x,y))
                a = dfs(x+1, y, visited, pointer+1)
                b = dfs(x, y+1, visited, pointer+1)
                c = dfs(x, y-1, visited, pointer+1)
                d = dfs(x-1, y, visited, pointer+1)
                visited.remove((x,y))
                return (a or b or c or d)

                # a = dfs(x+1, y, visited, pointer+1)
            else:
                return False
            
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]==word[0]:
                    visited = set()
                    d = dfs(x,y,visited)
                    if d is True:
                        return True
        return False