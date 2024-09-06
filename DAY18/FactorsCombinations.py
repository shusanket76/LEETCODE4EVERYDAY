class Solution:
  def getFactors(self, n):
    # TODO: Write your code here
    factors = []
    res = []
    midn = n//2
    for x in range(2, midn+1):
      if n%x==0:
        factors.append(x)
    def dfs(curr, pointer, n):
      if n==1:
        if len(curr)>0:
          res.append(curr[:])
        return 
      if pointer==len(factors) or n<1:
        return 
      curr.append(factors[pointer])
      dfs(curr, pointer, n/factors[pointer])
      curr.pop()
      dfs(curr, pointer+1, n)
    
    curr = []
    pointer = 0
    dfs(curr, pointer, n)
    return (res)
    # return []
