class Solution:
  def canPartition(self, num, sum):
    # Write you code here


    def dfs(pointer, num, target):
      if target==0:
        return True
      if target<0 or pointer>=len(num):
        return False
      a = dfs(pointer+1, num, target-num[pointer])
      if a is True:
        return True
      b = dfs(pointer+1, num, target)
      if b is True:
        return True
      return False
    
    pointer = 0
    res = dfs(pointer, num, target = sum)
    return res 
