class Solution:
  def floodFill(self, matrix, x, y, newColor):
    # TODO: Write your code here
    visited = set()
    def dfs(x, y, defaultcolor):
      if x>=0 and y>=0 and x<len(matrix) and y<len(matrix[0]) and matrix[x][y]==defaultcolor and (x,y) not in visited:
        visited.add((x,y))
        left = dfs(x+1,y,defaultcolor)
        right = dfs(x-1,y,defaultcolor)
        up = dfs(x,y+1,defaultcolor)
        down = dfs(x,y-1,defaultcolor)
        matrix[x][y]=newColor
        return 
      else:
        return 
    defaultcolor = matrix[x][y]
    dfs(x,y, defaultcolor)
    return matrix
