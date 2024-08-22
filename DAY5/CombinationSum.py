class Solution:
  def combinationSum(self, candidates, target):
    res = []  # To store the final result
    # TODO: Write your code here
    def dfs(curr, pointer, target):
      if target ==0:
        print(res)
        res.append(curr[:])
        return 
      if target<0 or pointer>=len(candidates):
        return 
      curr.append(candidates[pointer])
      dfs(curr, pointer, target - candidates[pointer])
      curr.pop()
      dfs(curr, pointer+1, target)
    
    dfs(curr = [], pointer=0, target=target)
    return res