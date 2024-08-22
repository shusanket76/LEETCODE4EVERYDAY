def solveKnapsack(profits, weights, capacity):
    # TODO: Write your code here
    res = [0]
    def dfs(w, p, pointer):
      if w>capacity or pointer>=len(weights):
        if w<=capacity:
           res
        return 
      res[0] = max(res[0], p)
      p+=profits[pointer]
      w+=weights[pointer]
      left = dfs(w, p, pointer+1)
      p-=profits[pointer]
      w-=weights[pointer]
      right = dfs(w, p, pointer+1)


    
    dfs(0,0, pointer=0)
    return res[0]


profits = [1,6,10,16]
weights = [1,2,3,5]
capacity = 7
solveKnapsack(profits, weights, capacity)